from module.button.b_statistik import *

def btn_stat(self):
  self.btn_stat = Button(self, text="STATISTIK"
                         , command=lambda: open_statistik(self)
                         , height=1, width=10, bg="black", fg="white", borderwidth=5, font="Times 10 bold")

def open_statistik(self):
  btn_back(self, "statistik")
  show_sts(self)
  chart_bar(self)
  hide_menu(self)
