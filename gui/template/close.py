from gui.template.show import *
from gui.template.hide import *

def close_test(self):
  hide_test(self)
  show_menu(self)
  self.soal = []
  self.cate = []
  self.answ = []
  self.entry = []
  self.lsoal = []