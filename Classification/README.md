
# 📊 Sınıflandırma Algoritmalarının Karşılaştırması

Bu çalışma, çeşitli sınıflandırma algoritmalarının avantajlarını ve dezavantajlarını karşılaştırmalı olarak sunar.

| **Model** | **Avantajları** | **Dezavantajları** |
|----------|------------------|---------------------|
| **Lojistik Regresyon** | Olasılıksal yaklaşım, özelliklerin istatistiksel önemi hakkında bilgi verir. | Lojistik Regresyon varsayımlarına bağlıdır. |
| **K-NN** | Anlaması basit, hızlı ve verimli. | Komşuların \(k\) sayısını doğru seçmek gerekir. |
| **SVM** | Sonuca ulaşma performansı iyi, aykırı değerlere karşı duyarlı değil, aşırı öğrenmeye (overfitting) karşı dayanıklıdır. | Doğrusal olmayan problemler için uygun değildir, yüksek boyutlu özellikler için en iyi seçenek değildir. |
| **Kernel SVM** | Doğrusal olmayan problemlerde yüksek performanslıdır, aykırı değerlere karşı dayanıklıdır, aşırı öğrenmeye karşı duyarlıdır. | Yüksek boyutlu özellikler için en iyi seçenek değildir, daha karmaşıktır. |
| **Naive Bayes** | Verimli, aykırı değerlere karşı önyargılı değildir, doğrusal olmayan problemler üzerinde çalışır, olasılıksal yaklaşımdır. | Özelliklerin aynı istatistiksel anlamlılığa sahip olduğu varsayımına dayanır. |
| **Karar Ağacı** | Yorumlaması kolaydır, özellik ölçeklendirmesi gerekmez, hem doğrusal hem de doğrusal olmayan problemler için uygundur. | Çok küçük veri kümelerinde zayıf sonuç verir, aşırı öğrenmeye (overfitting) yatkındır. |