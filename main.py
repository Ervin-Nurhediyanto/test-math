from module.main import *

class TesMat(Frame):
  def __init__(self, master):
    Frame.__init__(self, master)
    self.master = master
    self.initUI()

  def initUI(self):
    label_title(self.master)
    main_menu(self)

def main():
  root = Tk()
  root.geometry("1000x600")
  root.iconbitmap(os.path.join(sys.path[0]), "logo.ico")
  app = TesMat(root)
  root.mainloop()

if __name__ == "__main__":
  main()
