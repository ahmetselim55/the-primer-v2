# Proje Spec: The Primer v2 - Dikey Model Entegrasyonu

## 1. Model Gereksinimi ve Amaç
* *Hedef:* Geçtiğimiz hafta hazırladığımız "The Primer" hikayesine, oyuncunun davranışlarından öğrenen ve karar mekanizmasına etki eden küçük, göreve özel (dikey) bir yapay zeka modeli (model.onnx) entegre etmek[span_2](start_span)[span_2](end_span).
* *Kapsam:* Oyuncunun anlık durumuna (örn: seviye, karar_suresi, onceki_yanlis_sayisi, ipucu_sayisi, sahne_no) bakarak "Bu oyuncunun şu sahneye ipucuna ihtiyacı var mı?" sorusuna karar veren model[span_3](start_span)[span_3](end_span).

## 2. Eval Metriği
* *Metrik:* Doğruluk (Accuracy) ve F1-Score[span_4](start_span)[span_4](end_span).
* *Açıklama:* Modelin tahmin ettiği karar ile gerçek kullanıcı oturumlarındaki kararların uyum yüzdesi ölçülecektir.

## 3. Kabul Eşiği (Alt Standart)
* *Kriter:* Modelin canlıya (deploy) alınabilmesi için doğruluk oranının *en az %85 (0.85)* olması şarttır. Eşik eğitimden ÖNCE yazılmıştır; bu eşiği geçmeyen model kesinlikle yayınlanmaz[span_5](start_span)[span_5](end_span).

## 4. Yeni Kabul Örnekleri (Test Senaryoları)
1. *Örnek 1:* Oyuncu seviyesi yüksek ve karar süresi 10 saniyenin altındaysa model ipucu önermemelidir (ipucu_gerekli: 0).
2. *Örnek 2:* Oyuncu aynı sahnede üst üste 2 kez yanlış yaptıysa ve ipucu sayısı uygunsa model mutlaka ipucu önermelidir (ipucu_gerekli: 1).
3. *Örnek 3:* Hızlı geçilen sahnelerde taban tolerans kurallarına göre sistem karar değiştirmeli, model eşiği geçilirse tutor baskısı kalkmalıdır[span_6](start_span)[span_6](end_span).