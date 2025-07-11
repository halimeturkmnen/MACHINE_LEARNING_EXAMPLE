import pandas as pd # veri analizi için (veri tutmak , data frame oluşturmak)
import numpy as np # veri işleme için (büyük veri seti, matematiksel işlemler)
import matplotlib.pyplot as plt # grafik çizimi için

# Veri setini yükleme
veriler = pd.read_csv(r"C:\Users\SD\OneDrive\Masaüstü\machine_learning_example\Data_Preprocessing_and_Prediction\veri_on_isleme\eksikveriler.csv") # csv dosyası dizini 
# dosya yolunda / yerine; \\ kullanabilirsiniz veya r"" kullanabilirsiniz veya / kullanabilirsiniz
print (veriler)
boy = veriler [["boy"]]
print (boy)
boyvekilo= veriler [["boy", "kilo"]]
print(boyvekilo)


# eksik veri tamir etme
from sklearn.impute import SimpleImputer 
imputer = SimpleImputer (missing_values = np.nan, strategy = "mean")
Yas = veriler.iloc [:,1:4].values # 1. sütundan 4. sütuna kadar olan verileri alır
print(Yas)
imputer = imputer.fit (Yas [:,1:4])  # eksik verileri tamir etmek için imputer nesnesini oluşturur
Yas [:,1:4] = imputer.transform (Yas[:,1:4]) # eksik verileri tamir eder 
print(Yas)


# Encoder ile nominal (kategorik) değerleri sayısal değerlere dönüştürme
ulke = veriler.iloc [:,0:1].values # 0. sütunda olan verileri alır
print(ulke)
from sklearn import preprocessing 
le = preprocessing .LabelEncoder() 
ulke[:,0] = le.fit_transform(veriler.iloc[:,0]) # ulke sütunundaki nominal değerleri sayısal değerlere dönüştürür
print(ulke)
ohe = preprocessing .OneHotEncoder()
ulke= ohe.fit_transform(ulke).toarray() # ulke sütunundaki sayısal değerleri one hot encoding ile dönüştürür
print(ulke)


# Veriyi birleştirme
sonuc = pd.DataFrame (data=ulke, index = range(22),columns = ['fr', 'tr', 'us']) # ulke numpy dizisini data frame'e çevirir
print(sonuc)
sonuc2 = pd.DataFrame (data=Yas, index = range(22), columns = ['boy', 'kilo', 'yas'])
print(sonuc2)
cinsiyet = veriler.iloc[:,-1].values
print(cinsiyet)
sonuc3 = pd.DataFrame(data=cinsiyet, index= range(22),columns = ['cinsiyet'])
print(sonuc3)
s= pd.concat([sonuc,sonuc2], axis=1) # ulke ve yas dataframe'lerini birleştirir
print(s)
s2=pd.concat([s,sonuc3], axis=1) # cinsiyet dataframe'ini de ekler
print(s2)


# Veriyi eğitim ve test setlerine ayırma
from sklearn.model_selection import train_test_split 
x_train, x_test, y_train, y_test = train_test_split (s, sonuc3, test_size = 0.33, random_state= 0) # test seti %33, eğitim seti %67
print(x_train)
print(x_test) 
print(y_train)
print(y_test)


# Özellik ölçekleme
from sklearn.preprocessing import StandardScaler    
sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform (x_test)
print(X_train)
print(X_test)
