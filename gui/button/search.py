from module.button.b_search import *

def btn_search(self):
  self.btn_search = Button(self, text="SEARCH"
                         , command=lambda: filter_list(self)
                        , height=1, width=10, bg="#47B5FF", fg="white", borderwidth=5, font="Times 10 bold")

def filter_list(self):
  close_table(self)
  data_r(self)

  self.list_data_filter = []
  if self.search.get() == "Nama":
    self.search_key = self.entry_search.get()
  elif self.search.get() == "Nilai":
    self.search_key = int(self.entry_search.get())

  for i in range(len(self.list_data)):
    if self.search.get() == "Nama":
      is_filter = self.search_key in self.list_data[i][self.search.get()]
    elif self.search.get() == "Nilai":
      is_filter = self.search_key == self.list_data[i][self.search.get()]
    if is_filter:
      self.list_data_filter.append(self.list_data[i])
  self.list_data = self.list_data_filter

  open_table(self)

def close_table(self):
  hide_entry_table_h(self)
  hide_entry_table_d(self)

def open_table(self):
  table_h(self)
  table_d(self)
