import os
from paddleocr import PaddleOCR
from PIL import Image
import numpy as np

if __name__ == "__main__":
    ocr = PaddleOCR(lang='fr')
    img_path = os.path.join("data","streaters.jpg")
    img = np.asarray(Image.open(img_path))
    result = ocr.ocr(img,cls=False)
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            print(line)
    