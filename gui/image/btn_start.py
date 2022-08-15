import os
import sys
from PIL import Image, ImageTk

def img_btn_start(self):
  path = "{}\\asset\start_button.png".format(os.path.join(sys.path[0]))
  image = Image.open(path)
  resize_image = image.resize((100, 100))
  self.img_btn_start = ImageTk.PhotoImage(resize_image)

# img_btn_start(self)
  # self.btn_test = Button(self, image = self.img_btn_start
  #                        , command=lambda: reg_user(self, self.entry_name.get())
  #                        , height=30, width=80)
  # self.btn_test.image = self.img_btn_start