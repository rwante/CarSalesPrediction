import pandas as pd
from sklearn import linear_model,model_selection, preprocessing
from sklearn.model_selection import train_test_split
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from scipy import stats
from sklearn.ensemble import BaggingRegressor
from sklearn import tree
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import GradientBoostingRegressor
import xgboost as xgb
import matplotlib


df = pd.read_csv('data.csv', sep=';')
for c in df.columns:#Dosyadaki stringleri sayiya çevirme // Categorical Feature Encoding
    if df[c].dtype == 'object':
        lbl = preprocessing.LabelEncoder()
        #lbl.fit(list(df[c].values))
        df[c] = lbl.fit_transform(list(df[c].values))
"""
dummy = pd.get_dummies(df['Marka'])#Dummy Variables
df = pd.concat([df,dummy],axis=1)
df = df.drop(["Marka"],axis=1)
dummy = pd.get_dummies(df['Yakit'])
df = pd.concat([df,dummy],axis=1)
df = df.drop(["Yakit"],axis=1)
"""
for i in range(0,10):#Normalizasyon 0-1 arasina degerleri sikistirma
    sutun_ismi = df.columns[i]
    en_dusuk = np.min(df[sutun_ismi])
    en_buyuk = np.max(df[sutun_ismi])
    df[sutun_ismi] = ((df[sutun_ismi])-en_dusuk)/(en_buyuk-en_dusuk)
X = df.drop(["Fiyat"],axis=1)
Y = df['Fiyat']
X = df.drop(["Model"],axis=1)
data_train, data_test, label_train, label_test = train_test_split(X,Y, test_size=0.3,random_state=23)
"""
plt.scatter(data_test['Km'],A,color="blue",label="predict")
plt.scatter(data_train['Km'],label_train,color="green",label="train")
plt.scatter(data_test['Km'],label_test,color="red",label="test")
plt.legend()
plt.show()
"""
"""
print(regr.score(data_train,label_train))
print(regr.score(data_test,label_test))


model = BaggingRegressor(tree.DecisionTreeRegressor(random_state=42))
model.fit(data_train,label_train)
print(model.score(data_train,label_train))
print(model.score(data_test,label_test))
print(model.predict(data_test))
print(label_test)
"""
"""
model = AdaBoostRegressor()
model.fit(data_train, label_train)
print(model.score(data_train,label_train))
print(model.score(data_test,label_test))
print(model.predict(data_test))
print(label_test)
"""
"""
model= GradientBoostingRegressor()
model.fit(data_train, label_train)
print(model.score(data_train,label_train))
print(model.score(data_test,label_test))
print(model.predict(data_test))
print(label_test)
"""
model=xgb.XGBRegressor()
model.fit(data_train, label_train)
print(model)
print(model.score(data_train,label_train)*100)
print(model.score(data_test,label_test)*100)
tahmin = model.predict(data_test)
out = pd.DataFrame({'Actual_price': label_test, 'predict_price': tahmin.astype(int),'Hata' :(label_test-tahmin)})
print(out)



"""
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
"""