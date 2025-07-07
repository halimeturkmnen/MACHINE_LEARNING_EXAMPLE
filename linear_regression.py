import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


veriler = pd.read_csv(r"C:\Users\SD\OneDrive\Masaüstü\machine_learning_example\satislar.csv")
print(veriler)

aylar = veriler[["Aylar"]]
print(aylar)
satislar = veriler[["Satislar"]]
print(satislar)
# satislar2 = veriler.iloc [:,:].values

from sklearn.model_selection import train_test_split 
x_train, x_test, y_train, y_test = train_test_split(aylar,satislar, test_size=0.33, random_state=0) # random_state: rastgelelik için sabit bir değer belirler, böylece her seferinde aynı sonuçları alırız.
print(x_train)
print(x_test)
print(y_train)
print(y_test)
'''
from sklearn.preprocessing import StandardScaler # şunun için kullanıyoruz: Özellik ölçekleme, modelin daha iyi performans göstermesini sağlar.
sc = StandardScaler()
X_train = sc.fit_transform(x_train) # fit_transform: eğitim verilerini ölçekler ve dönüşüm uygular.
X_test = sc.transform(x_test) 

Y_train = sc.fit_transform(y_train) 
Y_test = sc.transform(y_test)
'''
# model inşası (linear regression)
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train, y_train) # fit: modelin train verileri üzerinde öğrenmesini sağlar.
tahmin = lr.predict(x_test) #  x_test’teki ay değerlerine bak, ve satış değerlerini tahmin et. biz bunu y_test ile karşılaştıracağız, .predict() fonksiyonu girdi bekler, çıktı değil.
print("Tahmin Edilen Satis Degerleri:")
print(tahmin)

x_train = x_train.sort_index() # x_train verilerini sıralar
y_train = y_train.sort_index() # y_train verilerini sıralar

plt.plot(x_train, y_train)
plt.plot(x_test, lr.predict(x_test))
plt.title("Satis Tahmin Grafiği")
plt.xlabel("Aylar")
plt.ylabel("Satislar")
plt.show()
