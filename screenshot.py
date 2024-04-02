from PIL import ImageGrab

def screenshot():
    img = ImageGrab.grab()
    return img