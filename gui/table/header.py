from gui.entry.table.header import *
from gui.template.show import *

def table_h(self):
  table_header = ("ID", "NAMA", "NILAI")
  self.table_H = []
  self.table_HR = []
  for i in range(len(table_header)):
    self.table_H.append(None)
    self.table_HR.append(None)
    w = 10
    if i == 1:
      w = 50
    entry_table_h(self, i, w)
    entry_table_hr(self, i, w)
    show_entry_table_h(self, i)
    self.table_H[i].insert(END, table_header[i])
    if len(self.list_data) > 25:
      show_entry_table_hr(self, i)
      self.table_HR[i].insert(END, table_header[i])
