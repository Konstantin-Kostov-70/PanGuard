# PAN Card Tempering Detection App

## Overview

This is a Flask-based web application that allows users to upload a PAN card image and compare it with an existing, original image of a PAN card using computer vision techniques. The app utilizes image processing libraries such as OpenCV and Skimage to compute the structural similarity between the uploaded and the original images and highlights any visual differences.

## Features

- **Image Upload**: Users can upload their PAN card image for comparison.
- **Image Comparison**: The app compares the uploaded image with an existing original image using structural similarity index (SSIM).
- **Image Processing**: The app processes both the uploaded and original images by converting them to grayscale and resizing them to ensure they match in size.
- **Difference Detection**: It calculates and visualizes differences between the two images, showing contours around the mismatched areas.
- **Visual Output**: The original, uploaded, and difference images are generated and saved, allowing for visual inspection.

## Requirements

### Python Packages
Ensure you have the following Python libraries installed:

- Flask
- Pillow (PIL)
- OpenCV (`cv2`)
- Skimage (Scikit-image)
- Imutils
- dotenv (optional, if using environment variables for configuration)

You can install the required packages using the following command:

```bash
pip install Flask Pillow opencv-python scikit-image imutils python-dotenv
```
## Installation

1. Clone the repository to your local machine:

```bash
    git clone https://github.com/Konstantin-Kostov-70/Pan-Card-Tempering.git
    cd Pan-Card-Tempering
```
2. Set up a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```
3. Install the dependencies:

```bash
pip install -r requirements.txt
```
4. Configure file paths for the images:

- The original PAN card image should be placed in app/static/original/ directory as image.jpg.
- Uploaded PAN card images will be saved to app/static/uploads/.
- The generated output images (original with contours, uploaded with contours, difference images) will be saved in app/static/generated/.

5. Run the app:

```bash
python app.py
```

## File Structure
```
├── app/
│   ├── static/
│   │   ├── uploads/       # Folder to store uploaded images
│   │   ├── original/      # Folder to store the original image (image.jpg)
│   │   └── generated/     # Folder to store generated result images
│   ├── templates/
│   │   └── index.html     # HTML file for the UI
│   └── app.py             # Main Flask application
├── README.md
└── requirements.txt       # List of required dependencies
```
## How It Works
1. Upload Image: The user uploads a PAN card image via the web interface.

2. Resizing and Preprocessing: Both the uploaded image and the original image are resized to ensure they match in size (250x160 in this case) for better     comparison.

3. Image Comparison: The app converts both the uploaded and the original images into grayscale, and calculates the Structural Similarity Index (SSIM) between the two images. This index measures how similar or different the two images are

4. Thresholding and Contour Detection: Based on the SSIM result, a difference image is computed. The difference is then thresholded to highlight areas where the images differ, and contours are drawn around those areas.

5. Results: The SSIM score is displayed on the webpage, indicating how similar the uploaded PAN card is to the original. The images with highlighted differences (original, uploaded, and difference) are saved in the app/static/generated/ directory.

## Running the App
1. Open your browser and navigate to http://127.0.0.1:5000/.
2. Upload a PAN card image to compare it with the original.
3. The app will display the similarity score and visually highlight the differences between the two images.

## Example Output
- SSIM Score: The similarity score will be displayed as a percentage, e.g., 95.5% correct.
- Image Differences: The contours around the differences between the original and the uploaded PAN card will be shown.

## Future Improvements
- Support for multiple file uploads.
- A more sophisticated UI for displaying the generated images and differences.
- Improved image alignment and rotation handling for better accuracy.
- Integration of environment variable configuration for secret management.

## License
- This project is licensed under the MIT License. Feel free to use it and contribute to its improvement.