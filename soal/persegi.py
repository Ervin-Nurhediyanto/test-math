from bangun_datar.persegi import Formula

class SoalPersegi():
  def __init__(self, s):
    self.s = s
    self.f = Formula(self.s)
    self.question = "Sebuah persegi memiliki panjang sisi " + str(self.s) + "."

  def q_luas(self):
    self.question = self.question + " Berapakah luas persegi tersebut?"
    return self.question

  def a_luas(self, answer):
    self.ans_is_not_numb = True
    self.answer = answer

    if self.answer == self.f.luas():
      return 20
    else:
      return 0

  def q_kell(self):
    self.question = self.question + " Berapakah keliling persegi tersebut?"
    return self.question

  def a_kell(self, answer):
    self.ans_is_not_numb = True
    self.answer = answer

    if self.answer == self.f.keliling():
      return 20
    else:
      return 0
