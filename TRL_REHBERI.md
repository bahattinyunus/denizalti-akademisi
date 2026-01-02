# 🌊 Denizaltı Teknolojileri Hazırlık Seviyesi (TRL) Rehberi

Bu rehber, denizaltı ve su altı sistemleri projelerinin olgunluk seviyelerini (Technology Readiness Levels - TRL) belirlemek için kullanılır. NASA ve savunma sanayi standartlarının denizaltı teknolojilerine uyarlanmış halidir.

## 📊 TRL Seviyeleri ve Tanımları

| TRL | Seviye Adı | Denizaltı Teknolojileri İçin Tanım | Örnek Durum |
| :--- | :--- | :--- | :--- |
| **TRL 1** | **Temel Prensipler** | Temel fiziksel/kimyasal prensiplerin denizaltı sistemlerine (akustik, hidrodinamik, basınç) uygulanabilirliği kağıt üzerinde araştırılmıştır. | Yeni bir sonar algoritması için teorik matematiksel modelin oluşturulması. |
| **TRL 2** | **Teknoloji Konsepti** | Pratik uygulama fikirleri formüle edilmiştir. Teori ile pratik uygulama arasında bağ kurulmuştur. | Yeni bir batarya kimyasının denizaltı enerji profilini nasıl etkileyeceğine dair raporlar. |
| **TRL 3** | **Deneysel Kanıt (PoC)** | Kritik fonksiyonların laboratuvar ortamında analitik veya deneysel olarak doğrulanması (Proof of Concept). | Küçük bir basınç tankında yeni bir gövde malzemesinin test edilmesi. |
| **TRL 4** | **Laboratuvarda Doğrulama** | Bileşen veya alt sistemin laboratuvar ortamında entegre edilip çalıştırılması. | Yeni bir torpido motorunun laboratuvar tezgahında çalıştırılması. |
| **TRL 5** | **İlgili Ortamda Doğrulama** | Bileşen veya alt sistemin, gerçek çalışma koşullarına benzer (simüle edilmiş) bir ortamda test edilmesi. | Bir UUV sensörünün kontrollü bir havuzda test edilmesi. |
| **TRL 6** | **İlgili Ortamda Demo** | Sistemin veya prototipin ilgili ortamda (deniz, havuz, basınç odası) tam fonksiyonel demosu. | Bir insansız denizaltının sığ sularda otonom görev icra etmesi. |
| **TRL 7** | **Operasyonel Ortamda Demo** | Sistemin gerçek operasyonel koşullarda (açık deniz, derin su) prototip demosu. | Yeni bir sonar sisteminin askeri bir gemiye monte edilip denizde test edilmesi. |
| **TRL 8** | **Tamamlanmış Sistem** | Sistemin son halini alması ve tüm testlerden (kalifikasyon) başarıyla geçmesi. | Sistemin seri üretime hazır hale gelmesi, tüm sertifikasyonların alınması. |
| **TRL 9** | **Operasyonel Kanıt** | Sistemin gerçek görevlerde başarıyla kullanıldığının kanıtlanması (Combat Proven / Mission Proven). | Sistemin donanma envanterine girmesi ve aktif görevde kullanılması. |

---

## 🎯 Bu Repo Nasıl Kullanılır?

Her teknoloji alanı (İtki, Savaş Sistemleri, vb.) altındaki `PROJELER.md` dosyasında, takip edilen projeler bu TRL seviyelerine göre sınıflandırılır.

**Örnek Proje Girişi:**

```markdown
### [TRL 4] Lityum-Sülfür Batarya Teknolojisi
- **Durum:** Laboratuvar prototipi test ediliyor.
- **Hedef:** Mevcut Li-Ion bataryalara göre %40 daha fazla enerji yoğunluğu.
- **Son Güncelleme:** 2024-05
- **İlgili Dosyalar:** [Rapor v1](./docs/lis_rapor.pdf)
```
