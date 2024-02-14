from tkinter import *
from PIL import ImageTk, Image
import cv2
import random
import numpy as np
import math
root = Tk()
root.resizable(False, False)
global ds
ds = 10

class ImageHandeling:
    def __init__(self, image, canvas, initial, c, cnv) -> None:
        self.x = 550
        self.c = c
        self.y = 350
        self.dx = -1
        self.count = 0
        self.img = Image.open(image)
        self.cnv = cnv
        self.obs = ImageTk.PhotoImage(self.img)
        self.canvas = canvas
        self.width = cv2.imread(image).shape[0]
        self.image_item = canvas.create_image(self.x, self.y, image=self.obs)

    def alongX(self):
        self.canvas.move(self.image_item, self.dx, 0) 
        borderLimit = abs(canvas.coords(self.image_item)[0] - self.width)
        if (borderLimit <= 729):
                self.canvas.after(10, self.alongX)
        else:
            render = random.randint(1, 4)
            self.dx -= 0.5
            image = ImageHandeling(f't{render}.png', self.canvas, False, self.c + 1, self.cnv)
            root.after(ds, image.alongX)

    def getCoordinates(self):
        return canvas.coords(self.image_item)
    
    def endGame(self):
        pass

class Projectile:
     def __init__(self, canvas) -> None:
          self.characterImage = "proj.png"
          self.pathImg = Image.open(self.characterImage)
          self.character = self.pathImg.resize((50, 50), Image.LANCZOS)
          self.projectile = ImageTk.PhotoImage(self.character)
          self.x = 200
          self.y = 300
          self.canvas = canvas
          self.dy = 1 # constant for character
          self.set_projectile = canvas.create_image(self.x, self.y, image=self.projectile)
          self.dProjectileHold = 0
          self.positiveHold = 2
          self.theta = 0
          self.intial  = True
          self.end = False
          self.maxima = 480

     def getCanvas(self):
        return canvas.coords(self.set_projectile)

     def vectorNegativeY(self):
            characterCoordinates = canvas.coords(self.set_projectile)
            y =  500 - characterCoordinates[1] # static height of the frame 500
            if y >= self.maxima:
               return
            self.nY = True
            if self.intial is True:
                 self.canvas.move(self.set_projectile, 5, self.dy) 
                 self.intial = False
            else:
              self.canvas.move(self.set_projectile, 0, self.dy) 
            self.vectorYneg = True
            # negative y till the bottom limit
            if (y >= 25):
                root.after(ds, self.vectorNegativeY) # terminating interval negative y if positive y is true
     def vectorPositiveY(self):
          characterCoordinates = canvas.coords(self.set_projectile)
          y =  500 - characterCoordinates[1]
          if y >= self.maxima:
               return
          # for only d time
          self.dy = -1.2
          self.positiveHold += 1
          if (self.positiveHold <= 25 ):
               root.after(ds, self.vectorPositiveY) 
          else:
                 self.positiveHold = 0
                 self.dy = 1

root.geometry("500x500")
root.title("AAVASH")
canvas = Canvas(root, width=500, height=500, bg="#9F44D3")
canvas.pack()
projectile = Projectile(canvas)
projectile.vectorNegativeY() # intially -y axis
root.bind('<space>', lambda event: projectile.vectorPositiveY())
root.after(ds, projectile.vectorNegativeY)
im = ImageHandeling("t1.png", canvas, True, 0, projectile.getCanvas())
im.alongX() 
root.mainloop()
