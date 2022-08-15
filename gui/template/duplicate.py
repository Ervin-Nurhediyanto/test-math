def duplicate_name(self, name):
  self.duplicate_name = False
  for i in range(len(self.list_data)):
    if name.upper() == self.list_data[i]["Nama"].upper():
      self.duplicate_name = True
