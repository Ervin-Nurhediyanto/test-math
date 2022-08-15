from tkinter import *

def op_src_by(self):
  OPTIONS = [
    "Nama",
    "Nilai"
  ]
  self.search = StringVar(self.master)
  self.search.set(OPTIONS[0])
  self.op_src_by = OptionMenu(self.master, self.search, *OPTIONS)
