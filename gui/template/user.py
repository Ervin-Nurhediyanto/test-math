from tkinter import *
from gui.template.data import *
from gui.template.menu import *
from gui.template.msg import *

def reg_user(self, name):
  self.score = 0
  if name:
    data_r(self)
    data_n(self, name)
    data_c(self)
    hide_menu(self)

  else:
    msg_reg_fail()