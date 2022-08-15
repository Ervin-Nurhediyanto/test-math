from tkinter import *

def label_test(self, i):
  self.lsoal.append(None)
  if (i % 2 == 0):
    self.cate.append('luas')
    label_test_luas(self, i)
  else:
    self.cate.append('kell')
    label_test_kell(self, i)

def label_test_luas(self, i):
  self.lsoal[i] = Label(self.master, text="No {}. {}"
    .format(str(i + 1), self.soal[i].q_luas()))

def label_test_kell(self, i):
  self.lsoal[i] = Label(self.master, text="No {}. {}"
    .format(str(i + 1), self.soal[i].q_kell()))
