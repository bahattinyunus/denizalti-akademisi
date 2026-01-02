# 2_SISTEMLER: Sensör Füzyonu ve Akustik Dizilimler

## 📡 Modern Sonar Mimarisi

Bir denizaltı sadece burnundaki sonar ile görmez. Tüm gövdesi ve arkasından sürüklediği sensörler ile devasa bir akustik antene dönüşür.

### 1. Dizilim Tipleri (Arrays)
- **Küresel Burun Sonarı (Sphere):** 360 dereceye yakın yatay tarama sağlar. Hem aktif hem pasif modda çalışır.
- **Flank Array (Yan Dizilim):** Denizaltının her iki yanına boylu boyunca yerleştirilen panellerdir. Çok düşük frekanslı sesleri tespit edebilir.
- **Towed Array (Sürüklenen Dizilim):** Denizaltının arkasından yüzlerce metre kablo ile çekilen hidrofon dizisidir. Geminin kendi gürültüsünden uzak olduğu için en hassas sensördür.

### 2. Sensör Füzyonu (LOFAR/DEMON)
Farklı sensörlerden gelen veriler, sinyal işleme sistemlerinde birleştirilir:
*   **LOFAR (Low Frequency Analysis):** Dar bantlı sinyalleri analiz ederek hedefin tipini belirler.
*   **DEMON (Detection of Envelope Modulation on Noise):** Pervane sesindeki modülasyonu analiz ederek hedefin pervanesi kanat sayısını ve devrini ölçer.

---

## 🛰️ Optronik Sensörler

Modern denizaltılarda (örn. Virginia, Astute) klasik optik periskopların yerini **Fotonik Mastlar** almıştır. Fiber optik kablolar ile veri aktarımı yapan bu sistemler, basınç gövdesinde delik açılmasını engeller.

---
*“Sessizliği dinlemek, en büyük teknolojik üstünlüktür.”*
