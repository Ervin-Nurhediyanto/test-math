def hide_menu(self):
  hide_label_name(self)
  hide_entry_name(self)
  hide_btn_test(self)
  hide_btn_list(self)
  hide_btn_stat(self)
  hide_img_menu(self)

def hide_test(self):
  hide_label_test(self)
  hide_entry_test(self)
  hide_btn_submit(self)
  hide_img_test(self)

def hide_list(self):
  hide_op_src_by(self)
  hide_entry_search(self)
  hide_btn_search(self)
  hide_entry_table_h(self)
  hide_entry_table_d(self)

# Label
def hide_label_name(self):
  self.label_name.place_forget()

def hide_label_test(self):
  for i in range(len(self.lsoal)):
    self.lsoal[i].place_forget()

# Entry
def hide_entry_name(self):
  self.entry_name.place_forget()

def hide_entry_search(self):
  self.entry_search.place_forget()

def hide_entry_test(self):
  for i in range(len(self.entry)):
    self.entry[i].place_forget()

def hide_entry_table_h(self):
  for i in range(3):
    self.table_H[i].place_forget()
  if len(self.list_data) > 25:
    for i in range(3):
	    self.table_HR[i].place_forget()

def hide_entry_table_d(self):
  for i in range(len(self.list_data)):
    if i < 25:
      for j in range(3):
        self.table_D[i][j].place_forget()
    if i >= 25:
      for j in range(3):
        self.table_DR[i-25][j].place_forget()

# Button
def hide_btn_test(self):
  self.btn_test.place_forget()

def hide_btn_submit(self):
  self.btn_submit.place_forget()

def hide_btn_list(self):
  self.btn_list.place_forget()

def hide_btn_stat(self):
  self.btn_stat.place_forget()

def hide_btn_back(self):
  self.btn_back.place_forget()

def hide_btn_search(self):
  self.btn_search.place_forget()

# Image
def hide_img_menu(self):
  self.label_img_menu.place_forget()

def hide_img_test(self):
  self.label_img_test.place_forget()

# Option
def hide_op_src_by(self):
  self.op_src_by.place_forget()
