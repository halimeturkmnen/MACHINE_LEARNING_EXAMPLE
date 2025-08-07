# Deep Learning ile Müşteri Terk (Churn) Tahmini

Bu proje, bir bankanın müşterilerine ait veriler üzerinden yapay sinir ağı (ANN) kullanılarak müşterinin bankadan ayrılıp ayrılmayacağını (churn) tahmin etmeyi amaçlar.

## 📁 Proje İçeriği

- `9.1 - Kütüphanelerin kurulum komutları.docx`: Projede kullanılan derin öğrenme kütüphanelerinin kurulum adımlarını içerir.
- `9.2 - ann.py`: Veri ön işleme, yapay sinir ağı modeli oluşturma, eğitme ve tahmin sürecini içeren Python betiğidir.
- `Churn_Modelling.csv`: Müşteri verilerini içeren veri kümesidir.

## 🧪 Kullanılan Kütüphaneler

Projede aşağıdaki Python kütüphaneleri kullanılmıştır:

- **NumPy**: Sayısal işlemler için
- **Pandas**: Veri yükleme ve işleme
- **Matplotlib**: Görselleştirme
- **Scikit-learn**: Ön işleme, veri bölme, ölçekleme ve metrikler
- **Keras**: Yapay sinir ağı oluşturma ve eğitme

Kurulum komutları:

```bash
# Theano kurulumu
pip install –upgrade –no-deps git+git://github.com/Theano/Theano.git
# veya
conda install theano

# Keras kurulumu
pip install –upgrade keras
# veya
conda install -c conda-forge/label/cf201901 keras

# TensorFlow kurulumu
pip3 install –upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.8.0-py3-none-any.whl
# veya
conda create -n tensorflow python=3.7
```

## 🧠 Yapay Sinir Ağı Modeli

Python dosyasında (`ann.py`) gerçekleştirilen adımlar:

1. **Veri Yükleme**: `Churn_Modelling.csv` dosyasından veri alınır.
2. **Ön İşleme**:
   - Kategorik veriler sayısal verilere dönüştürülür (Label Encoding ve One-Hot Encoding).
   - Eğitim ve test veri setlerine bölme.
   - Ölçekleme (StandardScaler).
3. **Modelleme**:
   - Keras kullanılarak `Sequential` model tanımlanır.
   - 2 gizli katman ve 1 çıktı katmanı kullanılır.
   - Aktivasyon fonksiyonları olarak `relu` ve `sigmoid` tercih edilmiştir.
4. **Model Eğitimi**:
   - `adam` optimizasyon algoritması
   - `binary_crossentropy` kayıp fonksiyonu
   - 50 epoch boyunca eğitim
5. **Tahmin ve Değerlendirme**:
   - Tahmin edilen sonuçlar ve gerçek değerler karşılaştırılır.
   - Confusion matrix ile doğruluk değerlendirilir.

## 📊 Veri Kümesi: `Churn_Modelling.csv`

Bu veri kümesi, müşterilerin çeşitli özelliklerini (ülke, cinsiyet, kredi skoru, bakiye vb.) içerir ve `Exited` sütunu, müşterinin bankadan ayrılıp ayrılmadığını gösterir.

| Sütun Adı        | Açıklama                       |
|------------------|--------------------------------|
| CreditScore      | Kredi skoru                    |
| Geography        | Müşterinin ülkesi              |
| Gender           | Cinsiyet                       |
| Age              | Yaş                            |
| Tenure           | Bankadaki yıl sayısı           |
| Balance          | Hesap bakiyesi                 |
| NumOfProducts    | Kullandığı ürün sayısı         |
| HasCrCard        | Kredi kartı sahibi mi?         |
| IsActiveMember   | Aktif müşteri mi?              |
| EstimatedSalary  | Tahmini maaşı                  |
| Exited           | Bankadan ayrıldı mı? (hedef)   |

## 🚀 Nasıl Çalıştırılır?

1. Gerekli kütüphaneleri yükleyin.
2. `ann.py` dosyasındaki veri yolu (`read_csv`) kendi dizininize göre güncelleyin.
3. Python betiğini çalıştırarak modeli eğitip test edin.

```bash
python ann.py
```