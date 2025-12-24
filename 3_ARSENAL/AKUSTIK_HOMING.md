# 3_ARSENAL: Akustik Güdüm ve Torpido Mantığı

## 🎯 Akustik Homing (Hedefe Yönelme)

Modern torpidolar, hedefin yaydığı sesleri (Pasif Homing) veya kendi yaydığı seslerin yankısını (Aktif Homing) kullanarak hedefe kilitlenir.

### 1. Pasif Homing Mantığı
Torpido burnundaki hidrofon dizini ($A$), hedefin ses kaynağını ($S$) tespit eder. Sinyalin iki hidrofon arasındaki varış zaman farkı ($\Delta t$), hedefin açısını belirler:

$$\theta = \arcsin\left(\frac{c \cdot \Delta t}{d}\right)$$

*   $c$: Ses hızı (Su altında $\sim 1500 m/s$)
*   $d$: Hidrofonlar arası mesafe

### 2. Aktif Homing ve Doppler Etkisi
Torpido bir ses sinyali gönderir ve yankıyı dinler. Yankıdaki frekans kayması ($f_d$), hedefin hızını belirler:

$$f_d = \frac{2 \cdot v \cdot f_0}{c}$$

*   $v$: Hedefin yaklaşma hızı
*   $f_0$: Gönderilen frekans

---

## 🛡️ Karşı Tedbirler (Countermeasures)

| Tedbir | Çalışma Prensibi |
| :--- | :--- |
| **Decoy (Sahte Hedef)** | Denizaltı sesini taklit eden küçük araçlar. |
| **Jammer (Gürültücü)** | Torpido sonarını sağır eden yüksek gürültü yayımı. |
| **Anekoik Kaplama** | Torpido sonar sinyallerini emen gövde katmanı. |

---
*Vurmak bir seçenek, kilitlenmek bir sanattır.*
