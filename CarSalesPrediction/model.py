import pandas as pd
from sklearn import linear_model
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


df = pd.read_csv('data2.csv', sep=';')

X = df[['Yil',
        'Km']]
Y = df['Fiyat']

regr = linear_model.LinearRegression()
regr.fit(X, Y)

# tkinter GUI
root = tk.Tk()

canvas1 = tk.Canvas(root, width=500, height=300)
canvas1.pack()


label1 = tk.Label(root, text='\tYıl: ')
canvas1.create_window(100, 100, window=label1)

entry1 = tk.Entry(root)  # create 1st entry box
canvas1.create_window(270, 100, window=entry1)

label2 = tk.Label(root, text=' Km: ')
canvas1.create_window(120, 120, window=label2)

entry2 = tk.Entry(root)  # create 2nd entry box
canvas1.create_window(270, 120, window=entry2)


def values():
        global yil
        yil = float(entry1.get())

        global km
        km = float(entry2.get())

        Prediction_result = (
        'Fiyat: ', regr.predict([[yil, km]]))
        label_Prediction = tk.Label(root, text=Prediction_result, bg='orange')
        canvas1.create_window(260, 280, window=label_Prediction)


button1 = tk.Button(root, text='Fiyat', command=values,
                    bg='orange')
canvas1.create_window(270, 150, window=button1)


figure3 = plt.Figure(figsize=(5, 4), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df['Yil'].astype(float), df['Km'].astype(float), color='r')
scatter3 = FigureCanvasTkAgg(figure3, root)
scatter3.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
ax3.legend(['Fiyat'])
ax3.set_xlabel('Yıl')
ax3.set_title('Yıl Vs. Fiyat')


figure4 = plt.Figure(figsize=(5, 4), dpi=100)
ax4 = figure4.add_subplot(111)
ax4.scatter(df['Km'].astype(float), df['Fiyat'].astype(float), color='g')
scatter4 = FigureCanvasTkAgg(figure4, root)
scatter4.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
ax4.legend(['Fiyat'])
ax4.set_xlabel('Km')
ax4.set_title('Km Vs. Fiyat')

root.mainloop()