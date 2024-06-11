# Bounding Box to Polygon Conversion Tool

## Overview

This repository contains a Python script designed to convert bounding boxes into polygons for image segmentation tasks. The script processes directories of images and their corresponding annotation files, extracts polygon segmentation data, and generates cropped images based on these polygons. The cropped images are then saved in a structured directory based on their category.(This simple python code will let you draw and extract polygons from an image by using bounding box coordinates)

## Features

- **Directory Scanning**: Recursively scans a given directory to locate subdirectories containing image and annotation files.
- **JSON Annotation Parsing**: Reads JSON files to extract image segmentation and category information.
- **Polygon Drawing**: Draws polygons on images using the segmentation data and creates masks to crop the relevant image sections.
- **Image Cropping and Saving**: Crops the images according to the polygon masks and saves them in a structured format based on their category.
