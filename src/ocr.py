import numpy as np

def ocrize(img,model):
    result = model.ocr(np.asarray(img),cls=False)
    return result[0]
