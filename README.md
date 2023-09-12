
<!-- # NeutrEx -->
<h1 align="center"> NeutrEx: A 3D Quality Component Measure on Facial Expression Neutrality</h1>
<p align="center">

  <p align="center">
    <a href="https://www.ntnu.no/ansatte/marceg"><strong>Marcel Grimmer</strong></a>    
    ·
    <a href="https://dasec.h-da.de/staff/christian-rathgeb/"><strong>Christian Rathgeb</strong></a>
    ·
    <a href="https://people.utwente.nl/r.n.j.veldhuis"><strong>Raymond Veldhuis</strong></a>
    ·
    <a href="https://www.ntnu.edu/employees/christoph.busch"><strong>Christoph Busch</strong></a>

  </p>
  <h2 align="center">IJCB 2023</h2>
  <div align="center">
  </div>

  <!-- <a href="">
    <img src="./assets/teaser.jpeg" alt="Logo" width="100%">
  </a> -->

This repository contains the official implementation of the [IJCB 2023](https://ijcb2023.ieee-biometrics.org/) paper [NeutrEx: A 3D Quality Component Measure on Facial Expression Neutrality](https://arxiv.org/abs/2308.09963). 


<p align="center"> 
<img src="classwise-neutrex-vals.JPG">
</p>


EMOCA takes a single in-the-wild image as input and reconstructs a 3D face with sufficient facial expression detail to convey the emotional state of the input image. EMOCA advances the state-of-the-art monocular face reconstruction in-the-wild, putting emphasis on accurate capture of emotional content. The official project page is [here](https://emoca.is.tue.mpg.de/index.html).


## Installation 

Please follow the setup instructions of [EMOCA](https://github.com/radekd91/emoca) to create a conda environment ("work38"), download pre-trained models, and pull additional dependencies.     


## Usage 

0) Activate the environment: 
```bash
conda activate work38_cu11
```

1) For running EMOCA examples, go to [EMOCA](gdl_apps/EMOCA) 

2) For running examples of Emotion Recognition, go to [EmotionRecognition](gdl_apps/EmotionRecognition)

## Citation 

If you use this work in your publication, please cite the following publications:

```
@inproceedings{NeutrEx:IJCB:2023,
  title = {{NeutrEx}: {A} 3D Quality Component Measure on Facial Expression Neutrality},
  author = {Grimmer, Marcel and Rathgeb, Christian, Veldhuis, Raymond and Busch, Christoph},
  journal = {arXiv preprint arXiv:2308.09963}
  year = {2023}
}
```
```
@inproceedings{EMOCA:CVPR:2021,
  title = {{EMOCA}: {E}motion Driven Monocular Face Capture and Animation},
  author = {Danecek, Radek and Black, Michael J. and Bolkart, Timo},
  booktitle = {Conference on Computer Vision and Pattern Recognition (CVPR)},
  pages = {20311--20322},
  year = {2022}
}
```
As EMOCA builds on top of [DECA](https://github.com/YadiraF/DECA) and uses parts of DECA as fixed part of the model, please further cite:
```
@article{DECA:Siggraph2021,
  title={Learning an Animatable Detailed {3D} Face Model from In-The-Wild Images},
  author={Feng, Yao and Feng, Haiwen and Black, Michael J. and Bolkart, Timo},
  journal = {ACM Transactions on Graphics (ToG), Proc. SIGGRAPH},
  volume = {40}, 
  number = {8}, 
  year = {2021}, 
  url = {https://doi.org/10.1145/3450626.3459936} 
}
```
Furthermore, if you use EMOCA v2, please also cite [SPECTRE](https://filby89.github.io/spectre/): 
```
@article{filntisis2022visual,
  title = {Visual Speech-Aware Perceptual 3D Facial Expression Reconstruction from Videos},
  author = {Filntisis, Panagiotis P. and Retsinas, George and Paraperas-Papantoniou, Foivos and Katsamanis, Athanasios and Roussos, Anastasios and Maragos, Petros},
  journal = {arXiv preprint arXiv:2207.11094},
  publisher = {arXiv},
  year = {2022},
}
```

## License
This code and model are **available for non-commercial scientific research purposes** as defined in the [LICENSE](https://emoca.is.tue.mpg.de/license.html) file. By downloading and using the code and model you agree to the terms of this license. 

## Acknowledgements 
There are many people who deserve to get credited. These include but are not limited to: 
Yao Feng and Haiwen Feng and their original implementation of [DECA](https://github.com/YadiraF/DECA).
Antoine Toisoul and colleagues for [EmoNet](https://github.com/face-analysis/emonet).
