def show_menu(self):
  show_label_name(self)
  show_entry_name(self)
  show_btn_test(self)
  show_btn_list(self)
  show_btn_stat(self)
  show_img_menu(self)

def show_test(self):
  show_label_test(self)
  show_entry_test(self)
  show_btn_submit(self)
  show_img_test(self)

def show_sts(self):
  show_btn_back_sts(self)

def show_list(self):
  show_btn_back(self)
  show_op_src_by(self)
  show_btn_search(self)
  show_entry_search(self)

# Label
def show_label_name(self):
  self.label_name.place(relx=0.02, rely=0.15, anchor='w')

def show_label_test(self):
  for i in range(len(self.lsoal)):
    self.lsoal[i].place(relx=0.02, rely=0.25 + i*0.08, anchor='w')

# Entry
def show_entry_name(self):
  self.entry_name.place(relx=0.15, rely=0.15, anchor='w')

def show_entry_search(self):
  self.entry_search.place(relx=0.5, rely=0.15, anchor='center')

def show_entry_test(self):
  for i in range(len(self.entry)):
    self.entry[i].place(relx=0.98, rely=0.25 + i*0.08, anchor='e')

def show_entry_table_h(self, i):
  self.table_H[i].place(relx=0.05+0.18*i, rely=0.2, anchor='center')

def show_entry_table_hr(self, i):
  self.table_HR[i].place(relx=0.55+0.18*i, rely=0.2, anchor='center')

def show_entry_table_d(self, i, j):
  self.table_D[i][j].place(relx=0.05+0.18*j, rely=0.235+0.03*i, anchor='center')

def show_entry_table_dr(self, i, j):
  self.table_DR[i][j].place(relx=0.55+0.18*j, rely=0.235+0.03*i, anchor='center')

# Button
def show_btn_test(self):
  self.btn_test.place(relx=0.55, rely=0.15, anchor='e')

def show_btn_submit(self):
  self.btn_submit.place(relx=0.5, rely=0.8, anchor='center')

def show_btn_list(self):
  self.btn_list.place(relx=0.68, rely=0.15, anchor='e')

def show_btn_stat(self):
  self.btn_stat.place(relx=0.775, rely=0.15, anchor='e')

def show_btn_back(self):
  self.btn_back.place(relx=0.02, rely=0.15, anchor='w')

def show_btn_back_sts(self):
  self.btn_back.place(relx=0.02, rely=0.75, anchor='w')

def show_btn_search(self):
  self.btn_search.place(relx=0.625, rely=0.15, anchor='w')

# Image
def show_img_menu(self):
  self.label_img_menu.place(relx=0.5, rely=0.7, anchor='center')

def show_img_test(self):
  self.label_img_test.place(relx=0.875, rely=0.83, anchor='center')

# Option
def show_op_src_by(self):
  self.op_src_by.place(relx=0.375, rely=0.15, anchor='e')
