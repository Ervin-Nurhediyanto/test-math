from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from gui.template.chart.bar.data import *

def chart_bar(self):
  chart_data(self)
  self.figure = plt.Figure(figsize=(6,5), dpi=100)
  self.ax = self.figure.add_subplot(1, 1, 1)
  self.bar = FigureCanvasTkAgg(self.figure, self.master)
  self.bar.get_tk_widget().pack(side=BOTTOM, fill=BOTH)
  self.df_dc = self.df_dc[['Nilai','Frekuensi']].groupby('Nilai').sum()
  self.df_dc.plot(kind='bar', legend=True, ax=self.ax)
  self.ax.set_title('Data Statistik Tes Matematika')
  self.ax.set_xlabel("Nilai Matematika")
  self.ax.set_ylabel("Frekuensi")
  plt.margins(x=0, y=0)
