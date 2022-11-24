import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)

def isCollide(data):
    for i in range(620,730):
        for j in range(250,340):
          if data[i,j] < 100 :
            return True
    return False

if __name__ == "__main__":
    print("Hey champ...Dino game about to start in 3 seconds")
    time.sleep(3)
    hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if isCollide(data):
           hit('up')
        # print(asarray(image))
        
        #for i in range(620,700):
        #  for j in range(280,330):
        #      data[i,j]=0

        #image.show()
        
      
      