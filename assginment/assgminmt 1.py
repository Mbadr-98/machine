import cv2 as cv
import matplotlib.pyplot as plt

# Read the image
image_path = 'id.jpeg'  # Correct path for the uploaded image
image = cv.imread(image_path)

# Resize image to match the ID size (adjustable to your needs)
image_resized = cv.resize(image, (400, 600))

# Draw the three required rectangles
cv.rectangle(image_resized, (100, 100), (150, 200), (255, 0, 0), 2)
cv.rectangle(image_resized, (200, 200), (300, 300), (0, 255, 0), 2)
cv.rectangle(image_resized, (250, 320), (400, 400), (0, 0, 255), 2)

# Add text (Name)
font = cv.FONT_HERSHEY_SIMPLEX
org = (150, 525)
fontScale = 1
color = (200, 25, 0)
thickness = 2
cv.putText(image_resized, 'Mohamed Badr', org, font, fontScale, color, thickness, cv.LINE_AA)

# Draw black circles on the corners
cv.circle(image_resized, (0, 0), 50, (0, 0, 0), -1)
cv.circle(image_resized, (0, image_resized.shape[0] - 1), 50, (0, 0, 0), -1)
cv.circle(image_resized, (image_resized.shape[1] - 1, 0), 50, (0, 0, 0), -1)
cv.circle(image_resized, (image_resized.shape[1] - 1, image_resized.shape[0] - 1), 50, (0, 0, 0), -1)

# Draw line under the name
cv.line(image_resized, (org[0] - 20, org[1] + 10), (org[0] + 250, org[1] + 10), (0, 0, 255), thickness=3)

# Transparency handling using 4 subplots
Titles = ["1", "2", "3", "4"]
images = [image_resized, image_resized, image_resized, image_resized]  # Same image for all transparency levels
alphas = [1.0, 0.25, 0.40, 0.70]  # Different transparency levels
count = 4

# Display the images in subplots with transparency
plt.figure(figsize=(10, 10))
for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])

    # Convert to RGB (from BGR) and apply transparency using matplotlib's alpha
    plt.imshow(cv.cvtColor(images[i], cv.COLOR_BGR2RGB), alpha=alphas[i])  # Convert to RGB and apply transparency
    plt.axis('off')

plt.show()