import json
from tkinter import *
from gui.template.msg import *
from gui.template.answ import *
from gui.template.data import *
from gui.template.close import *
from gui.template.hide import *

def btn_submit(self):
  self.btn_submit = Button(self, text="SUBMIT"
                           , command=lambda: submit(self)
                           , height=2, width=10, bg="#C1EFFF", fg="#0F3D3E", borderwidth=5, font="Times 10 bold")

def submit(self):
  MsgBox = msg_ask_ques()
  if MsgBox == 'yes':
    user_answ(self)
    if self.total_answ < 5:
      msg_war_reansw()
    else:
      check_user_answ(self)
      msg_res_test(self)
      data_r(self)
      for i in range(len(self.list_data)):
        if self.list_data[i]["Nama"] == self.entry_name.get():
          self.list_data[i]["Nilai"] = self.score
        self.list_data[i] = json.dumps(self.list_data[i])
      data_update = ';'.join(self.list_data)
      data_u(self, data_update)
      self.score = 0
      self.total_answ = 0
      close_test(self)
      hide_btn_back(self)
