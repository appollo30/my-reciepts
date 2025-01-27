import os
from src.reader import read_image
from src.ocr import ocrize
import matplotlib.pyplot as plt
from paddleocr import draw_ocr
from PIL import Image

def draw_results(img,result,lang="french"):
    # Path for font to draw
    font_path = os.path.join(".","data","fonts",f"{lang}.ttf")
    print(font_path)
    # Actual drawing
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = Image.fromarray(draw_ocr(img, boxes, txts, scores, font_path=font_path))
    im_show.show()

if __name__ == "__main__":
    img_path = "streaters.jpg"
    img = read_image(img_path)
    result = ocrize(img)
    draw_results(img,result)
    