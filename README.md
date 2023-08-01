# I2T_ocr
This repository contains a Python program that performs Optical Character Recognition (OCR) on images using the Tesseract OCR engine. The program applies various image preprocessing techniques to enhance the accuracy of OCR results, particularly for challenging images with noise, text skew, and varying backgrounds.
Key Features:

Image Preprocessing: The program applies a series of image preprocessing steps, including noise removal, thresholding, dilation, erosion, Canny edge detection, and skew correction. These techniques help clean up the image and improve the extraction of text regions for OCR.
Deskewing: The program incorporates advanced deskewing techniques to correct tilted or skewed text in the image. This helps to improve OCR accuracy for images with perspective distortion or uneven angles.
Tesseract OCR: The program utilizes the powerful Tesseract OCR engine for text extraction. It supports multiple languages and provides accurate results for a wide range of texts in the images.
Usage:

Note:

Ensure you have the necessary libraries installed, including OpenCV (opencv-python) and pytesseract (pytesseract).
Adjust the image preprocessing parameters as needed to achieve the best results for your images.
Contributions and Feedback:
Contributions and feedback are welcome! If you have any suggestions or improvements to enhance the OCR accuracy or add new features, please feel free to open an issue or submit a pull request.
