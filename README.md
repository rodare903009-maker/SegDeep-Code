# SegDeep-Code
Source code for generating diffusion-based deepfake and face-swap manipulations and their corresponding pixel-level segmentation masks.

## Dataset

The complete SegDeep dataset is available on Zenodo:

SegDeep Dataset — Zenodo

## Requirements

The code can be executed locally or using Google Colab. For large-scale datasets, Google Drive can be used to provide the required storage space.


# Dataset Generation Pipeline

The SegDeep dataset can be generated using the following steps.

## 1. Collect the source images

First, collect the source images required to construct the dataset.

For example, when using the FFHQ dataset, download the original images from the official source and place them in the corresponding input directory.

The source images should be organized according to the structure expected by the dataset preparation scripts.

## 2. Prepare and split the dataset

If additional Python packages are required, install them using:

```bash
pip install -r requirements.txt

```
For large datasets, the process may require a significant amount of storage space. 
Use the dataset preparation script to select and organize the source images into the groups required for SegDeep.

```bash
python build_segdeep_dataset.py zip_file.zip ./output skip_images
```

## 3. Generate face-swap manipulations

The face-swap generation process is provided as a Jupyter Notebook designed to run in Google Colab.

Open directly in Google Colab: 

Or simply click: <a href="https://colab.research.google.com/github/rodare903009-maker/SegDeep-Code/blob/main/Faceswap.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

Open faceswap.ipynb in Google Colab

The notebook generates the face-swap manipulated images and their corresponding pixel-level masks used in the SegDeep dataset.

| Face swap | Segmentation Mask | Face Swap Image | Segmentation Mask |
|:---:|:---:|:---:|:---:|
| <img src="Deepfake%20Images/Images/12000.png" width="160"> | <img src="Deepfake%20Images/Masks/12000.png" width="160"> | <img src="Deepfake%20Images/Images/12018.png" width="160"> | <img src="Deepfake%20Images/Masks/12018.png" width="160"> |
| <img src="Deepfake%20Images/Images/12011.png" width="160"> | <img src="Deepfake%20Images/Masks/12011.png" width="160"> | <img src="Deepfake%20Images/Images/12026.png" width="160"> | <img src="Deepfake%20Images/Masks/12026.png" width="160"> |

## 4. Generate deepfake manipulations

The deepfake generation process is provided as a Jupyter Notebook designed to run in Google Colab.

Open directly in Google Colab: 

Or simply click: <a href="https://colab.research.google.com/github/rodare903009-maker/SegDeep-Code/blob/main/Deepfake.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

Open Deepfake.ipynb in Google Colab

The notebook generates the face-swap manipulated images and their corresponding pixel-level masks used in the SegDeep dataset.

| Face swap | Segmentation Mask | Face Swap Image | Segmentation Mask |
|:---:|:---:|:---:|:---:|
| <img src="Deepfake%20Images/Images/12000.png" width="160"> | <img src="Deepfake%20Images/Masks/12000.png" width="160"> | <img src="Deepfake%20Images/Images/12018.png" width="160"> | <img src="Deepfake%20Images/Masks/12018.png" width="160"> |
| <img src="Deepfake%20Images/Images/12011.png" width="160"> | <img src="Deepfake%20Images/Masks/12011.png" width="160"> | <img src="Deepfake%20Images/Images/12026.png" width="160"> | <img src="Deepfake%20Images/Masks/12026.png" width="160"> |









