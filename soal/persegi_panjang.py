from bangun_datar.persegi_panjang import Formula

class SoalPersegiPanjang():
  def __init__(self, p, l):
    self.p = p
    self.l = l
    self.f = Formula(self.p, self.l)
    self.question = "Sebuah persegi panjang memiliki panjang " + str(self.p) + " dan lebar " + str(self.l)+"."

  def q_luas(self):
    self.question = self.question + " Berapakah luas persegi panjang tersebut?"
    return self.question

  def a_luas(self, answer):
    self.ans_is_not_numb = True
    self.answer = answer

    if self.answer == self.f.luas():
      return 20
    else:
      return 0

  def q_kell(self):
    self.question = self.question + " Berapakah keliling persegi panjang tersebut?"
    return self.question

  def a_kell(self, answer):
    self.ans_is_not_numb = True
    self.answer = answer

    if self.answer == self.f.keliling():
      return 20
    else:
      return 0
