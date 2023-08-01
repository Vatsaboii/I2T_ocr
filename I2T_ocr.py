import cv2
import pytesseract
import numpy as np

# Replace 'image_path' with the actual path to your image file
image_path = 'image_path.png'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
denoised_image = cv2.medianBlur(gray_image, 5)

# Thresholding (using binary inverse to make text appear white on black background)
_, threshold_image = cv2.threshold(denoised_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernel = np.ones((5, 5), np.uint8)
dilated_image = cv2.dilate(threshold_image, kernel, iterations=1)
eroded_image = cv2.erode(dilated_image, kernel, iterations=1)

# Canny edge detection (to detect the edges of the text regions)
edges_image = cv2.Canny(eroded_image, 50, 150, apertureSize=3)

# Detect the angle of the text lines using the Hough Line Transform
coords = np.column_stack(np.where(edges_image > 0))
angle = cv2.minAreaRect(coords)[-1]

# Correct the angle to deskew the image if the text is tilted
if angle < -45:
    angle = -(90 + angle)
else:
    angle = -angle

h, w = edges_image.shape[:2]
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

# Apply the rotation to deskew the image
rotated_image = cv2.warpAffine(eroded_image, rotation_matrix, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

# Resize the image after all the preprocessing steps (optional but can help improve OCR accuracy)
resized_image = cv2.resize(rotated_image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

# Specify the page segmentation mode and language for pytesseract
custom_config = r'--oem 3 --psm 6 -l eng'
text = pytesseract.image_to_string(resized_image, config=custom_config)
print(text)
