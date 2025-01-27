import os
from PIL import Image
import numpy as np

def read_image(file_name : str) -> Image:
    path = os.path.join("data",file_name)
    
    im = Image.open(path).convert("RGB")
    return im