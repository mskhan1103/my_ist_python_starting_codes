import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# ✅ Option 1: Use raw string for full absolute path
# Make sure to replace the path below with your actual image path
image_path = r"C:\Users\HTC\Documents\Numpy\practice examples\img\salman.jpg"

# ✅ Check if the file exists (optional but recommended)
if not os.path.exists(image_path):
    print("Error: File not found at", image_path)
else:
    # ✅ Read the image as a NumPy array
    img = mpimg.imread(image_path)

    # ✅ Convert RGB image to grayscale using weighted sum
    gray = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])

    # ✅ Display the original and grayscale images side by side
    plt.figure(figsize=(10, 4))

    # Original image
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title('Original Image')
    plt.axis('off')

    # Grayscale image
    plt.subplot(1, 2, 2)
    plt.imshow(gray, cmap='gray')  # 'gray' colormap to show in grayscale
    plt.title('Grayscale Image')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
