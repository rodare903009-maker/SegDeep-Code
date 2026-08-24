# -*- coding: utf-8 -*-
"""
SegDeep Dataset
FFHQ Dataset Preparation and Splitting

This script prepares the FFHQ dataset for the construction of the
SegDeep dataset by selecting and organizing the images into the
required subsets.

Author: Rodrigo Arevalo-Ancona
        Antonio Cedillo-Hernadez
        Manuel Cedllo-Hernandez
Project: SegDeep Dataset
"""

import os
import random
import zipfile

# ============================================================
# CONFIGURATION
# ============================================================

# Path to the ZIP file
ZIP_PATH = "archive (1).zip"

# Destination directory
OUTPUT_DIR = "swap5"

# Number of images to extract per execution
BATCH_SIZE = 1

# Number of images to skip
#
# Examples:
# SKIP = 0     → Images 0–9999
# SKIP = 10000 → Images 10000–19999
# SKIP = 20000 → Images 20000–29999
#
SKIP = 40000

# Seed for reproducibility
SEED = 42
random.seed(SEED)

# Allowed image file extensions
IMAGE_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".gif",
    ".webp",
    ".tiff",
)


# ============================================================
# MAIN EXECUTION
# ============================================================

# Create destination directory if it does not exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Open ZIP archive
with zipfile.ZipFile(ZIP_PATH, "r") as zip_ref:
    # Filter image files only
    images = [
        file for file in zip_ref.namelist()
        if file.lower().endswith(IMAGE_EXTENSIONS)
    ]

    # Sort files to maintain deterministic order
    images = sorted(images)
    total = len(images)

    print(f"\nTotal images found: {total}")

    # Validate range offset
    if SKIP >= total:
        raise ValueError(
            f"SKIP={SKIP} exceeds total available images ({total})"
        )

    # Slice the image batch
    selected_images = images[SKIP : SKIP + BATCH_SIZE]

    print(f"Skipping: {SKIP}")
    print(f"Extracting: {len(selected_images)}")

    # Extract selected files
    for file in selected_images:
        zip_ref.extract(file, OUTPUT_DIR)

print("\nProcess completed successfully.")
print(f"Images extracted: {len(selected_images)}")
print(f"Saved to: {OUTPUT_DIR}")