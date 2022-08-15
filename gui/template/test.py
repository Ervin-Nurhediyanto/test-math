from module.template.t_test import *

def rand_test(self, i):
  if (i == 0 or i == 1):
    self.soal.append(SoalPersegi(self.s))
  elif (i == 2 or i == 3):
    self.soal.append(SoalPersegiPanjang(self.p, self.l))
  elif (i == 4 or i == 5):
    self.soal.append(SoalLingkaran(self.r))
  elif (i == 6 or i == 7):
    self.soal.append(SoalBelahKetupat(self.s, self.d1, self.d2))

def open_test(self):
  params_test(self)
  self.pack(fill=BOTH, expand=1)
  for i in range(5):
    params(self)
    rand_test(self, self.list_number[i])
    label_test(self, i)
    self.answ.append(0)
    self.entry.append(None)
  for i in range(5):
    entry_test(self, i)
  img_test(self)
  btn_submit(self)
  show_test(self)
