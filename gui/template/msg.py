from tkinter import messagebox

def msg_reg_fail():
  messagebox.showinfo("PERINGATAN !!", "Nama tidak boleh kosong")

def msg_reg_duplicate(name):
  messagebox.showinfo("PERINGATAN !!", "Nama {} sudah mengikuti ujian".format(name))

def msg_ask_ques():
  return messagebox.askquestion("Jawaban Anda", "Yakin dengan jawaban anda?")

def msg_war_answ(i):
  messagebox.showinfo("Jawaban Anda", "Jawab hanya dengan angka untuk soal no {}.".format(i+1))

def msg_war_reansw():
  messagebox.showinfo("Jawaban Anda", "Silahkan lengkapi jawaban anda")

def msg_res_test(self):
  messagebox.showinfo("HASIL TES", "Tes telah berakhir. score anda: {}".format(self.score))
