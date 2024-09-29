# Voronoi Diagram Image Processing

This project implements Voronoi diagrams on images using different distance metrics. The program reads an image, applies a Voronoi partition based on randomly selected "germ" points, and colors each region accordingly. The distance metric used can be Euclidean, Manhattan, or Chebyshev, as chosen by the user.

## Features

- Applies Voronoi diagrams to images.
- Supports three distance metrics:
  - **Euclidean Distance**
  - **Manhattan Distance**
  - **Chebyshev Distance**
- Random selection of germ points.
- Visualization of the original image and the Voronoi diagram.

## Requirements

To run this project, you will need the following libraries installed:

- `numpy`
- `opencv-python` (only used for image reading)
- `Pillow`

You can install the required packages using:

```bash
pip install numpy opencv-python Pillow

