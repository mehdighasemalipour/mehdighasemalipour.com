import os
from PIL import Image

path = (
    "./"  # Replace with the actual path to your folder
)

for filename in os.listdir(path):
    if filename.lower().endswith(
        (".jpg", ".jpeg", ".png")
    ):  # Only process files with the .jpg, .jpeg, or .png extension
        img = Image.open(os.path.join(path, filename))
        new_filename = os.path.splitext(filename)[0] + ".webp"
        img.save(os.path.join(path, new_filename), "webp")
