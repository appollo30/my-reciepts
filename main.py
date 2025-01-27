from src.reader import read_image
from src.ocr import ocrize
from src.viz import visualize_results
import matplotlib.pyplot as plt
from PIL import Image

if __name__ == "__main__":
    img_path = "streaters.jpg"
    img = read_image(img_path)
    result = ocrize(img)
    viz = visualize_results(img,result)
    viz.show()
    