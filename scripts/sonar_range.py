"""
Denizalti Akademisi - Taktik Muhendislik Araclari
Sonar Range & Transmission Loss Calculator v1.0
"""

import math

def calculate_transmission_loss(range_m, factor=15):
    """
    Sualtinda ses yayilim kaybini hesaplar (db).
    TL = factor * log10(Range) + alpha * Range / 1000
    (factor: 20 kuresel, 10 silindirik yayilim)
    """
    if range_m <= 0: return 0
    absorption_coeff = 0.05 # db/km (Ornek deger)
    loss = factor * math.log10(range_m) + (absorption_coeff * range_m / 1000)
    return loss

def estimate_detection_range(source_level, noise_level, threshold):
    """
    Basit Sonar Denklemi: SL - TL - NL >= Threshold
    """
    # Basit bir iterasyon ile menzil tahmini
    for r in range(100, 50000, 100):
        tl = calculate_transmission_loss(r)
        if (source_level - tl - noise_level) < threshold:
            return r
    return 50000

if __name__ == "__main__":
    print("--- SUBSIM: AKUSTIK ANALIZ ---")
    
    sl = 130  # db (Hedef ses seviyesi)
    nl = 60   # db (Ortam gurultusu)
    dt = 10   # db (Tespit esigi)

    range_est = estimate_detection_range(sl, nl, dt)
    
    print(f"Hedef Kaynak Seviyesi: {sl} db")
    print(f"Ortam Gurultusu: {nl} db")
    print("-" * 30)
    print(f"TAHMINI TESPIT MENZILI: {range_est} metre")
