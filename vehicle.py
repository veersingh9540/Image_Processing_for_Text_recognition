import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

   
Data1 = {'PLACES': ['PLACE 1','PLACE 2','PLACE 3'],
        'VEHICLE': [45000,42000,52000]
       }

df1 = DataFrame(Data1, columns= ['PLACES', 'VEHICLE'])
df1 = df1[['PLACES', 'VEHICLE']].groupby('PLACES').sum()



Data2 = {'Time': [0000,1000,1200,1400,1500,1800,1900,2100,2200,2400],
        'Intensity_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
       }
  
df2 = DataFrame(Data2,columns=['Time','Intensity_Rate'])
df2 = df2[['Time', 'Intensity_Rate']].groupby('Time').sum()



Data3 = {'TIME': [5,5.5,6,5.5,5.25,6.5,7,8,7.5,8.5],
        'Cars': [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]
       }
  
df3 = DataFrame(Data3,columns=['TIME','Cars'])
 
  

root= tk.Tk() 
  

figure1 = plt.Figure(figsize=(5,9), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('PLACE POPULARITY')


figure2 = plt.Figure(figsize=(5,4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
ax2.set_title('Vehicle Passing BY ')


figure3 = plt.Figure(figsize=(5,4), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df3['TIME'],df3['Cars'], color = 'g')
scatter3 = FigureCanvasTkAgg(figure3, root) 
scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax3.legend() 
ax3.set_xlabel('HOURS')
ax3.set_title('NO of cars WRT time')

root.mainloop()