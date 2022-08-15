import os
import sys
import json

def data_r(self):
  self.list_user = os.path.join(sys.path[0], "list_nilai.txt")
  with open(self.list_user, "r") as f:
    self.data = f.read()
    f.close()
    replace_data = self.data.replace("'", '"')
  self.list_data = replace_data.split(";")
  self.list_data.pop()
  for i in range(len(self.list_data)):
    data = json.loads(self.list_data[i])
    self.list_data[i] = data

def data_c(self):
  with open(self.list_user, "w") as f:
    f.write('{}{};'.format(self.data, self.new_data))
    f.close()

def data_u(self, data):
  with open(self.list_user, "w") as f:
    f.write("{};".format(data))
    f.close()

def data_d(self):
  data_r(self)
  self.list_data.pop()
  for i in range(len(self.list_data)):
    self.list_data[i] = json.dumps(self.list_data[i])
  data_update = ';'.join(self.list_data)
  data_u(self, data_update)

def data_n(self, name):
  self.new_data = {
    "ID" : "{}".format(len(self.list_data) + 1),
		"Nama" : "{}".format(name),
		"Nilai" : "{}".format(self.score)
	}
