from module.button.b_test import *

def btn_test(self):
  self.btn_test = Button(self, text="MULAI TES"
                         , command=lambda: reg_user(self, self.entry_name.get())
                         , height=1, width=10, bg="black", fg="white", borderwidth=5, font="Times 10 bold")

def reg_user(self, name):
  self.score = 0
  if name:
    data_r(self)
    duplicate_name(self, name)
    if self.duplicate_name == True:
      msg_reg_duplicate(name)
    else:
      data_n(self, name)
      data_c(self)
      open_test(self)
      btn_back(self, 'test')
      show_btn_back(self)
      hide_menu(self)
  else:
    msg_reg_fail()
