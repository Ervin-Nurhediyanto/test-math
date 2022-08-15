class Formula():
  def __init__(self, s, d1, d2):
    self.s = s
    self.d1 = d1
    self.d2 = d2

  def keliling(self):
    return 4 * self.s

  def luas(self):
    return (self.d1 * self.d2)/2
