import matplotlib.pyplot as plt
import json
import time
from PIL import Image
import PIL.ImageOps    

GALAXY_IMAGE_PATH = f"data/galaxy_{time.time()}.png"
TYPES = {
    "ORANGE_STAR": "#008eff",
    "YOUNG_STAR": "#002bff",
    "HYPERGIANT": "#1ecdff",
    "WHITE_DWARF": "#00103e",
    "UNSTABLE": "#0653e9",
    "RED_STAR": "#00ffff",
    "NEUTRON_STAR": "#000707",
    "BLUE_STAR": "#8e7d00",
    "BLACK_HOLE": "#ffffff"
}

# Load the galaxy systems from the file
with open("data/galaxy.json", "r") as f:
    GALAXY = json.loads(f.read())

# Extract x and y coordinates from each system
x_coords = []
y_coords = []
system_color = []

for system in GALAXY:
    # Set the color of the system based on its type
    system_color.append(TYPES[system["type"]])
    x_coords.append(system["x"])
    y_coords.append(system["y"])

# Set the size of the plot
plt.figure(figsize=(10, 10))

# Plot the systems
plt.scatter(x_coords, y_coords, s=1, c=system_color)

# Add labels to the plot
plt.title("Galaxy Systems")

# Remove borders from the plot
plt.axis("off")

# Save the plot to a file
plt.savefig(GALAXY_IMAGE_PATH, dpi=300)

# Invert the image so that the background is black
image = Image.open(GALAXY_IMAGE_PATH)
image = image.convert("RGB")
inverted_image = PIL.ImageOps.invert(image)
inverted_image.save(GALAXY_IMAGE_PATH)