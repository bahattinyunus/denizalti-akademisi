# 1_MUHENDISLIK: Hidrostatik Analiz ve Basınç Fiziği

## 🌊 Derinlik ve Basınç Denklemleri

Denizaltı tasarımı, suyun derinliklerine indikçe artan muazzam hidrostatik basınca karşı koyma sanatıdı.

### 1. Hidrostatik Basınç Formülü
Sıvı basıncı ($P$), derinlik ($h$), sıvının yoğunluğu ($\rho$) ve yerçekimi ivmesine ($g$) bağlıdır:

$$P = \rho \cdot g \cdot h$$

*   **Örnek:** 1000m derinlikte, suyun yoğunluğu $\sim 1025 kg/m^3$ alındığında:
    - $P = 1025 \cdot 9.81 \cdot 1000 \approx 10,055,250 Pa \approx 100 atm$
    - Bu, santimetrekare başına $100 kg$ yük demektir.

### 2. Basınç Gövdesinde Gerilme (Hoop Stress)
Silindirik bir basınç gövdesinde oluşan çevresel gerilme ($\sigma$):

$$\sigma = \frac{P \cdot R}{t}$$

- $P$: Dış Basınç
- $R$: Gövde Yarıçapı
- $t$: Gövde Et Kalınlığı

**Mühendislik Kritiği:** Gövde materyalinin akma sınırı ($\sigma_y$), hesaplanan $\sigma$ değerinden emniyet katsayısı kadar büyük olmalıdır.

---

## 🧱 Malzeme Seçimi ve Mukavemet

| Malzeme | Akma Mukavemeti (MPa) | Avantajı |
| :--- | :--- | :--- |
| **HY-80 Çeliği** | 550 | Kaynaklanabilirlik |
| **HY-100 Çeliği** | 690 | Yüksek Mukavemet |
| **Titanyum (Ti-6Al-4V)** | 830 | Düşük Ağırlık / Korozyon Direnci |

---
*“Matematik, suyun altında hayatta kalmanın tek dilidir.”*
