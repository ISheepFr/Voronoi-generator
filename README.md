#Voronoi Diagram Image Processing
This project implements Voronoi diagrams on images using different distance metrics. The program reads an image, applies a Voronoi partition based on randomly selected "germ" points, and colors each region accordingly. The distance metric used can be Euclidean, Manhattan, or Chebyshev, as chosen by the user.

Features
Applies Voronoi diagrams to images.
Supports three distance metrics:
Euclidean Distance
Manhattan Distance (L1 Norm)
Chebyshev Distance (L∞ Norm)
Random selection of germ points.
Visualization of the original image and the Voronoi diagram.
Requirements
To run this project, you will need the following libraries installed:

numpy
opencv-python (only used for image reading)
Pillow
You can install the required packages using:

bash
Copier le code
pip install numpy opencv-python Pillow
Usage
Clone the repository:

bash
Copier le code
git clone https://github.com/yourusername/voronoi-image-processing.git
cd voronoi-image-processing
Run the script:

bash
Copier le code
python voronoi_discret.py <image_path> --dist <distance_metric>
<image_path>: Path to the input image.
<distance_metric>: Type of distance to be used:
0: Euclidean Distance
1: Manhattan Distance
2: Chebyshev Distance
Example
bash
Copier le code
python voronoi_discret.py input_image.jpg --dist 0
This command processes input_image.jpg using Euclidean distance and displays both the original image and the Voronoi partitioned image.

How It Works
Random Germ Selection: A number of random points (germs) are chosen based on the image size.
Distance Calculation: For each pixel in the image, the distance to each germ is computed using the selected distance metric.
Region Coloring: Each pixel is colored according to the nearest germ's color. Afterward, a smoothing process is applied by calculating the average color of each Voronoi region.
Note: OpenCV is used solely for opening and reading the images, while the rest of the processing is handled using numpy and Pillow.

Output
The resulting Voronoi image will be displayed, and a copy will be saved as end.jpg.

License
This project is licensed under the MIT License. See the LICENSE file for details.
