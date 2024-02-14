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

over = False

class ImageHandeling:
    def __init__(self, image, canvas, c, count) -> None:
        self.x = 550
        self.c = c
        canvas.itemconfig(count, text=f'count: {c}')
        self.y = 350
        self.dx = -1
        if c != 0:
             self.dx = self.dx - (c / 3)
        self.count = 0
        self.img = Image.open(image)
        self.obs = ImageTk.PhotoImage(self.img)
        self.canvas = canvas
        self.width = cv2.imread(image).shape[0]
        self.image_item = canvas.create_image(self.x, self.y, image=self.obs, tags="obs")

    def alongX(self):
        self.canvas.move(self.image_item, self.dx, 0) 
        borderLimit = abs(canvas.coords(self.image_item)[0] - self.width)
        if (borderLimit <= 729):
                self.canvas.after(10, self.alongX)
        else:
            render = random.randint(1, 5)
            self.dx -= 0.5
            image = ImageHandeling(f't{render}.png', self.canvas, self.c + 1, count)
            if over is False:
               root.after(ds, image.alongX)

    def getCoordinates(self):
        return canvas.coords(self.image_item)
    

    def endGame(self):
     if over is True:
          self.dx = 0
     # overlap check
     root.after(ds, self.endGame)
     


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
          self.set_projectile = canvas.create_image(self.x, self.y, image=self.projectile, tags="projectile")
          self.dProjectileHold = 0
          self.positiveHold = 2
          self.theta = 0
          self.intial  = True
          self.end = False
          self.maxima = 480

     def getCanvas(self):
        return canvas.coords(self.set_projectile)

     def vectorNegativeY(self):
            global over
            characterCoordinates = canvas.coords(self.set_projectile)
            y =  500 - characterCoordinates[1] # static height of the frame 500
            if y >= self.maxima:
               global over
               over = True
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
            else:
                 over = True
               
          
     def vectorPositiveY(self):
          characterCoordinates = canvas.coords(self.set_projectile)
          global over
          y =  500 - characterCoordinates[1]
          if y >= self.maxima:
               over = True
               return
          # for only d time
          self.dy = -1.3
          self.positiveHold += 1
          if (self.positiveHold <= 15 ):
               if y <= 25:
                    over = True
               root.after(ds, self.vectorPositiveY) 
          else:
                 self.positiveHold = 0
                 self.dy = 1

root.geometry("500x500")
root.title("CAPTAIN AAVASH FOREVER")
canvas = Canvas(root, width=500, height=500, bg="#9F44D3")
canvas.pack()
projectile = Projectile(canvas)
projectile.vectorNegativeY() # intially -y axis
root.bind('<space>', lambda event: projectile.vectorPositiveY())
root.after(ds, projectile.vectorNegativeY)
count = canvas.create_text(60, 20, text=f'count {0}', anchor="ne")
im = ImageHandeling("t1.png", canvas, 0, count)
im.alongX() 
im.endGame()
root.mainloop()
