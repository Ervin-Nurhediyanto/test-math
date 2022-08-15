from module.button.b_list import *

def btn_list(self):
  self.btn_list = Button(self, text="DAFTAR NILAI"
                         , command=lambda: open_list(self)
                         , height=1, width=15, bg="black", fg="white", borderwidth=5, font="Times 10 bold")

def open_list(self):
  btn_back(self, 'list')
  filter_data(self)
  data_r(self)
  table_h(self)
  table_d(self)
  hide_menu(self)
  show_list(self)

def filter_data(self):
  op_src_by(self)
  entry_search(self)
  btn_search(self)
