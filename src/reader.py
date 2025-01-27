import os
from PIL import Image

def read_image(file_name : str) -> Image:
    path = os.path.join("data",file_name)
    
    im = Image.open(path).convert("RGB")
    return im