import os
from paddleocr import PaddleOCR

if __name__ == "__main__":
    ocr = PaddleOCR(lang='fr')
    img_path = os.path.join("data","streaters.jpg")
    result = ocr.ocr(img_path,cls=False)
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            print(line)
    