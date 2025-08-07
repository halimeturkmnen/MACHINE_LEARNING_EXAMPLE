# Kümeleme (Clustering) Yöntemleri Karşılaştırması

Bu doküman, farklı kümeleme (clustering) yöntemlerinin karşılaştırmasını içermektedir. Özellikle **KMeans** ve **Hiyerarşik Kümeleme** algoritmaları ele alınmıştır.

## Karşılaştırma Tablosu

| Model                    | Artıları                                                                                                                                 | Eksileri                                                   |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| **KMeans**               | - Anlaşılması basittir  <br> - Mesafe metrikleri üzerinden çalışır  <br> - Küçük ve büyük veri setlerinde başarıyla uygulanabilir  <br> - Verimli ve performanslıdır | - Kaç bölüt/küme olacağına karar verilmesi gerekir         |
| **Hiyerarşik Kümeleme**  | - Farklı alternatiflerdeki küme sayıları için hazır şekilde bekler <br> - Model, en verimli küme sayısına karar verebilir <br> - Dendrogram ile görselleştirilebilir | - Büyük veri kümeleri için uygun değildir                 |

## Notlar

- **KMeans**, özellikle ölçeklenebilirliği sayesinde büyük veri kümelerinde tercih edilir.
- **Hiyerarşik yöntemler**, küçük veri kümeleri ve analiz odaklı görselleştirme için uygundur.