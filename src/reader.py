import os
from PIL import Image

def read_image(file_name : str) -> Image:
    path = os.path.join(".","data","img",file_name)

    img = Image.open(path).convert("RGB")
    return img
