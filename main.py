from PIL import Image
from pillow_heif import register_heif_opener


if __name__ == "__main__":
    register_heif_opener()
    path = "data/lidl.HEIC"
    im = Image.open(path,)
    im.show()
    