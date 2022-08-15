import random

def params(self):
  self.s = random.randint(1, 10)
  self.p = random.randint(1, 10)
  self.l = random.randint(1, 10)
  self.r = random.randint(1, 10)
  self.d1 = random.randint(1, 10)
  self.d2 = random.randint(1, 10)

  if self.p < self.l:
    self.p, self.l = self.l, self.p
  elif self.p == self.l:
    self.p += 1

def params_test(self):
  self.list_number = [x for x in range(8)]
  random.shuffle(self.list_number)
  self.soal = []
  self.cate = []
  self.lsoal = []
  self.answ = []
  self.entry = []
