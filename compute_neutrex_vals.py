# load modules
from gdl_apps.EMOCA.utils.load import load_model
from gdl.datasets.ImageTestDataset import TestData
from pathlib import Path
import gdl
import numpy as np
import pandas as pd
import os
import torch
from tqdm import tqdm
from tqdm import auto
import argparse
from gdl_apps.EMOCA.utils.io import generic_shape_test


parser = argparse.ArgumentParser(description='Arguments for computing NeutrEx values')
parser.add_argument('--indir', type=str, required = True,
                    help='Directory to face image folder')
parser.add_argument('--anchor_dir', required = True,
                    help='Path to neutral anchor (.npy)')

args = parser.parse_args()

# Input variables
path_to_models = str(Path(gdl.__file__).parents[1] / "assets/EMOCA/models")
indir = args.indir
neut_anchor_path = args.anchor_dir

# keep constant as empirically computed from MultiPIE and FEAFA+
D_MIN = 0.00045388718717731535
D_MAX = 0.008605152368545532


# Load EMOCA model
emoca, conf = load_model(path_to_models, "EMOCA_v2_lr_mse_20", "detail")
emoca.cuda()
emoca.eval()

# Create dataset from image folder
dataset = TestData(indir, face_detector="fan", max_detection=1)

# Load neutral anchor vertices
neut_anchor_verts = np.load(neut_anchor_path)
neut_anchor_verts = neut_anchor_verts.reshape(len(neut_anchor_verts) // 3, 3)

neutrex_vals = []
img_names = []
for img in tqdm(dataset):
    # load reconstruct input img and get vertices
    input_verts, _ = generic_shape_test(emoca, img)
    input_verts = input_verts['verts'][0].cpu().numpy()
    # compute neutrex vals (euclidean dists --> min-max-scaling)
    eucl_dist = np.linalg.norm(neut_anchor_verts - input_verts, ord = 2, axis = 1)
    avg_eucl_dist = np.mean(eucl_dist)
    neutrex_val = (avg_eucl_dist - D_MIN) / (D_MAX - D_MIN)
    neutrex_val = 100 * (1 - np.clip(neutrex_val, 0, 1))
    # Store vals and img names
    neutrex_vals.append(neutrex_val)
    img_names.append(img['image_name'][0])

    
results = pd.DataFrame({"img_name": img_names, "neutrex_scores": neutrex_vals})
results.to_csv(os.path.join(indir, "neutrex_results.csv"))
