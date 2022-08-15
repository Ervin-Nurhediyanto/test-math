from tkinter import *
from gui.entry.table.data import *
from gui.template.show import *

def table_d(self):
  self.table_D = []
  self.table_DR = []
  for i in range(len(self.list_data)):
    if i < 25:
      self.table_D.append([])
      for j in range(3):
        self.table_D[i].append(None)
        w = 10
        if j == 1:
          w = 50
        entry_table_d(self, i, j, w)
        show_entry_table_d(self, i, j)
        if j == 0:
          self.table_D[i][j].insert(END, self.list_data[i]["ID"])
        elif j == 1:
          self.table_D[i][j].insert(END, self.list_data[i]["Nama"])
        elif j == 2:
          self.table_D[i][j].insert(END, self.list_data[i]["Nilai"])
    elif (i >= 25 or i < 50):
      self.table_DR.append([])
      for j in range(3):
        self.table_DR[i-25].append(None)
        w = 10
        if j == 1:
          w = 50
        entry_table_dr(self, i-25, j, w)
        show_entry_table_dr(self, i-25, j)
        if j == 0:
          self.table_DR[i-25][j].insert(END, self.list_data[i]["ID"])
        elif j == 1:
          self.table_DR[i-25][j].insert(END, self.list_data[i]["Nama"])
        elif j == 2:
          self.table_DR[i-25][j].insert(END, self.list_data[i]["Nilai"])
