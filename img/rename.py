import os

path = "./"  # Replace with the actual path to your folder

i = 1
for filename in os.listdir(path):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):  # Only rename files with the .jpg, .jpeg, or .png extension
        extension = os.path.splitext(filename)[1].lower()
        new_filename = str(i) + extension
        os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
        i += 1
