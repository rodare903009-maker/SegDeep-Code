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
import sys
import random
import zipfile
import argparse

IMAGE_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".gif",
    ".webp",
    ".tiff",
)


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Extract a batch range of images from a ZIP archive."
    )
    parser.add_argument(
        "zip_path",
        type=str,
        help="Path to the source ZIP file."
    )
    parser.add_argument(
        "output_dir",
        type=str,
        help="Directory where extracted images will be saved."
    )
    parser.add_argument(
        "skip",
        type=int,
        help="Number of images to skip from the start."
    )
    parser.add_argument(
        "batch_size",
        type=int,
        nargs="?",
        default=None,
        help="Number of images to extract (optional, extracts all remaining if omitted)."
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for deterministic processing (default: 42)."
    )
    return parser.parse_args()


def extract_dataset(zip_path: str, output_dir: str, skip: int, batch_size: int | None, seed: int):
    """Handles the extraction of target images from the ZIP archive."""
    random.seed(seed)

    if not os.path.exists(zip_path):
        print(f"[ERROR] ZIP file not found at: {zip_path}")
        sys.exit(1)

    os.makedirs(output_dir, exist_ok=True)
    print(f"[INFO] Reading archive: {zip_path}")

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        # Filter supported image formats
        images = [
            f for f in zip_ref.namelist()
            if f.lower().endswith(IMAGE_EXTENSIONS)
        ]

        images = sorted(images)
        total_images = len(images)

        print(f"[INFO] Total images found: {total_images}")

        if skip >= total_images:
            print(f"[ERROR] Skip value ({skip}) exceeds total available images ({total_images}).")
            sys.exit(1)

        # Calculate extraction slice
        end_idx = total_images if batch_size is None else skip + batch_size
        selected_images = images[skip:end_idx]

        print(f"[INFO] Skipping first : {skip} images")
        print(f"[INFO] Extracting    : {len(selected_images)} images")

        for file in selected_images:
            zip_ref.extract(file, output_dir)

    print("\n" + "=" * 40)
    print(" Process Completed Successfully ")
    print("=" * 40)
    print(f"Extracted count : {len(selected_images)}")
    print(f"Saved location  : {output_dir}")


if __name__ == "__main__":
    args = parse_args()
    extract_dataset(
        zip_path=args.zip_path,
        output_dir=args.output_dir,
        skip=args.skip,
        batch_size=args.batch_size,
        seed=args.seed,
    )