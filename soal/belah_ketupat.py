from bangun_datar.belah_ketupat import Formula

class SoalBelahKetupat():
  def __init__(self, s, d1, d2):
    self.s = s
    self.d1 = d1
    self.d2 = d2
    self.f = Formula(self.s, self.d1, self.d2)
    self.question = "Sebuah belah ketupat memiliki panjang sisi " + str(self.s) + " dengan panjang diagonal " + str(self.d1) + " dan " + str(self.d2) +"."

  def q_luas(self):
    self.question = self.question + " Berapakah luas belah ketupat tersebut?"
    return self.question

  def a_luas(self, answer):
    self.ans_is_not_numb = True
    self.answer = answer

    if self.answer == self.f.luas():
      return 20
    else:
      return 0

  def q_kell(self):
    self.question = self.question + " Berapakah keliling belah ketupat tersebut?"
    return self.question

  def a_kell(self, answer):
    self.ans_is_not_numb = True
    self.answer = answer

    if self.answer == self.f.keliling():
      return 20
    else:
      return 0
