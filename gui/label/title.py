from tkinter import *
import tkinter.font

def label_title(master):
  master.title("TES MATEMATIKA")
  font_20 = tkinter.font.Font(size=20)
  title = Label(master, width=20, text="TES MATEMATIKA", font=font_20)
  title.place(relx=0.5, rely=0.05, anchor='center')
