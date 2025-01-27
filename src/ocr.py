from typing import List
import numpy as np
from PIL import Image
from paddleocr import PaddleOCR

def ocrize(img : Image, model : PaddleOCR) -> List:
    result = model.ocr(np.asarray(img),cls=False)
    return result[0]
