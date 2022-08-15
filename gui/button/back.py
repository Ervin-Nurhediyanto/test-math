from tkinter import *
from gui.template.data import *
from gui.template.hide import *
from gui.template.show import *

def btn_back(self, place):
  self.btn_back = Button(self, text="KEMBALI"
                         , command=lambda: back_to_menu(self, place)
                         , height=1, width=10, bg="#A10035", fg="white", borderwidth=5, font="Times 10 bold")

def back_to_menu(self, place):
  hide_btn_back(self)
  show_menu(self)
  if place == 'list':
    back_from_list(self)
  elif place == 'test':
    back_from_test(self)
  elif place == 'statistik':
    remove_plot(self.bar)

def back_from_list(self):
  hide_list(self)

def back_from_test(self):
  hide_test(self)
  data_d(self)

def remove_plot(canvas):
    canvas.get_tk_widget().destroy()
