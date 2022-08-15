from pandas import DataFrame
from gui.template.data import *

def chart_data(self):
  data_r(self)
  self.chart_data = [0, 0, 0, 0, 0, 0]
  scores = [0, 20, 40, 60, 80, 100]

  for i in range(len(self.list_data)):
    for j in range(len(scores)):
      if self.list_data[i]["Nilai"] == scores[j]:
        self.chart_data[j] += 1

  self.data_chart = {'Nilai': [0, 20, 40, 60, 80, 100],
    'Frekuensi': self.chart_data
  }
  self.df_dc = DataFrame(self.data_chart,columns=['Nilai','Frekuensi'])
