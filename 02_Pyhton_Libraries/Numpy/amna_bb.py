import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Create a blank white image
width, height = 400, 200
image = Image.new('RGB', (width, height), color='white')

# Draw text on the image
draw = ImageDraw.Draw(image)
text = "Amna BB"

# You can use default font or specify a .ttf font if available
font = ImageFont.load_default()
draw.text((50, 80), text, fill='black', font=font)

# Convert image to NumPy array
image_array = np.array(image)

# Save as .npy file
np.save("amna_bb.npy", image_array)
print("File 'amna_bb.npy' created successfully!")
