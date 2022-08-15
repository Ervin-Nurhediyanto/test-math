import os
import sys
from tkinter import *
from PIL import Image, ImageTk

def img_test(self):
  path = "{}\\asset\\test.png".format(os.path.join(sys.path[0]))
  image = Image.open(path)
  resize_image = image.resize((250, 200))
  self.img_test = ImageTk.PhotoImage(resize_image)
  self.label_img_test = Label(image=self.img_test)
  self.label_img_test.image = self.img_test
