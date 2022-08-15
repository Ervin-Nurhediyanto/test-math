from math import pi

class Formula():
  def __init__(self, r):
    self.r = r
    self.pi = round(pi, 2)

  def keliling(self):
    return round(2 * self.pi * self.r, 2)

  def luas(self):
    return round(self.pi * self.r ** 2, 2)
