from bangun_datar.lingkaran import Formula

class SoalLingkaran():
  def __init__(self, r):
    self.r = r
    self.f = Formula(self.r)
    self.question = "Sebuah lingkaran memiliki jari-jari " + str(self.r) + "."

  def q_luas(self):
    self.question = self.question + " Berapakah luas lingkaran tersebut? (pi = 3.14)"
    return self.question

  def a_luas(self, answer):
    self.ans_is_not_numb = True
    self.answer = answer

    if self.answer == self.f.luas():
      return 20
    else:
      return 0

  def q_kell(self):
    self.question = self.question + " Berapakah keliling lingkaran tersebut? (pi = 3.14)"
    return self.question

  def a_kell(self, answer):
    self.ans_is_not_numb = True
    self.answer = answer

    if self.answer == self.f.keliling():
      return 20
    else:
      return 0
