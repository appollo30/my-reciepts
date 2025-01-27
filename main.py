from paddleocr import PaddleOCR
from src.reader import read_image
from src.ocr import ocrize
from src.viz import visualize_results

if __name__ == "__main__":
    IMG_PATH = "streaters.jpg"
    img = read_image(IMG_PATH)
    model = PaddleOCR(lang="fr")
    result = ocrize(img,model=model)
    viz = visualize_results(img,result,draw=True)
    