from gui.template.msg import *

def input_answ(self, i):
  self.answ[i] = float(self.entry[i].get())

def user_answ(self):
  self.total_answ = 0
  for i in range(5):
    try:
      input_answ(self, i)
      self.total_answ += 1
    except:
      msg_war_answ(i)

def check_user_answ(self):
  for i in range(len(self.answ)):
    if self.cate[i] == 'luas':
      self.score += self.soal[i].a_luas(self.answ[i])
    else:
      self.score += self.soal[i].a_kell(self.answ[i])
