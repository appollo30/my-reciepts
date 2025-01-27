from paddleocr import PaddleOCR
import numpy as np

def ocrize(img):
    ocr = PaddleOCR(lang="fr")
    result = ocr.ocr(np.asarray(img),cls=False)
    return result[0]
