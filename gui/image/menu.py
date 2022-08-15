import os
import sys
from tkinter import *
from PIL import Image, ImageTk

def img_menu(self):
  path = "{}\\asset\menu.png".format(os.path.join(sys.path[0]))
  image = Image.open(path)
  resize_image = image.resize((500, 300))
  self.img_menu = ImageTk.PhotoImage(resize_image)
  self.label_img_menu = Label(image=self.img_menu)
  self.label_img_menu.image = self.img_menu
