
# Tahmin Metotları: SRL, MLR, PR, SVM, DT, RF ve Korelasyon

Bu proje; çeşitli regresyon yöntemlerini kullanarak tahmin modelleri kurmayı ve bunları korelasyon ve R² değerleri ile değerlendirmeyi amaçlamaktadır. Kullanılan yöntemler şunlardır:

## Kullanılan Kütüphaneler

- `numpy`
- `pandas`
- `matplotlib`
- `sklearn` (LinearRegression, PolynomialFeatures, SVR, DecisionTreeRegressor, RandomForestRegressor, StandardScaler)
- `statsmodels`

## Veri Yükleme

Veri dosyası: `maaslar_yeni.csv`

```python
veriler = pd.read_csv('maaslar_yeni.csv')
x = veriler.iloc[:,2:5]
y = veriler.iloc[:,5:]
X = x.values
Y = y.values
```

## Korelasyon Matrisi

Kolonlar arası ilişkileri incelemek için:

```python
print(veriler.corr())
```

## Yöntemler ve Kullanımları

### 1. Doğrusal Regresyon (Linear Regression)

```python
from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(X, Y)

model = sm.OLS(lin_reg.predict(X), X)
print(model.fit().summary())

print("Linear R2 değeri:")
print(r2_score(Y, lin_reg.predict(X)))
```

---

### 2. Polinom Regresyon (Polynomial Regression)

```python
from sklearn.preprocessing import PolynomialFeatures

poly_reg = PolynomialFeatures(degree=4)
x_poly = poly_reg.fit_transform(X)

lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly, y)

print(r2_score(Y, lin_reg2.predict(poly_reg.fit_transform(X))))
```

---

### 3. Destek Vektör Regresyonu (Support Vector Regression)

Veri ölçekleme ve model oluşturma:

```python
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

sc1 = StandardScaler()
x_scaled = sc1.fit_transform(X)

sc2 = StandardScaler()
y_scaled = np.ravel(sc2.fit_transform(Y.reshape(-1,1)))

svr_reg = SVR(kernel='rbf')
svr_reg.fit(x_scaled, y_scaled)

print(r2_score(y_scaled, svr_reg.predict(x_scaled)))
```

---

### 4. Karar Ağacı Regresyonu (Decision Tree)

```python
from sklearn.tree import DecisionTreeRegressor

r_dt = DecisionTreeRegressor(random_state=0)
r_dt.fit(X, Y)

print("Decision Tree R2 değeri:")
print(r2_score(Y, r_dt.predict(X)))
```

---

### 5. Rassal Orman Regresyonu (Random Forest)

```python
from sklearn.ensemble import RandomForestRegressor

rf_reg = RandomForestRegressor(n_estimators=10, random_state=0)
rf_reg.fit(X, Y.ravel())

print("Random Forest R2 değeri:")
print(r2_score(Y, rf_reg.predict(X)))
```

---

## Öğrenilenler

1. `scikit-learn` ile model oluşturma ve tahmin (fit/predict)
2. Korelasyon matrisinin önemi
3. Doğrusal, Polinom, SVR, Karar Ağacı ve Random Forest regresyonu arasındaki farklar
4. `r2_score` ve OLS çıktılarıyla karşılaştırma

---

## Gereksinimler

Aşağıdaki paketlerin yüklü olması gerekmektedir:

```bash
pip install numpy pandas matplotlib scikit-learn statsmodels
```

---

## Dosya Yapısı

- `maaslar_yeni.csv`: Girdi verileri
- `main.py`: Model kodları
- `README.md`: Bu dökümantasyon

---
