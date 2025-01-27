import os
from typing import List
from paddleocr import draw_ocr
from PIL import Image

def visualize_results(img : Image, result : List,
                      lang : str = "french", draw : bool = False) -> Image:
    # Path for font to draw
    font_path = os.path.join(".","data","fonts",f"{lang}.ttf")
    # Actual drawing
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = Image.fromarray(draw_ocr(img, boxes, txts, scores, font_path=font_path))
    if draw:
        im_show.show()
    return im_show
