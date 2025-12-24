"""
Denizalti Akademisi - Taktik Muhendislik Araclari
Underwater Sound Speed Calculator (Medwin Equation)
"""

def calculate_soundspeed(temp, salinity, depth):
    """
    Medwin Formulu kullanilarak su alti ses hizini (m/s) hesaplar.
    Gecerlilik: T [0-35 C], S [0-45 ppt], D [0-1000m]
    """
    # Medwin Equation
    c = 1449.2 + (4.6 * temp) - (0.055 * temp**2) + (0.00029 * temp**3) + \
        (1.34 - 0.01 * temp) * (salinity - 35) + (0.016 * depth)
    return c

if __name__ == "__main__":
    print("--- SUBSIM: SES HIZI HESAPLAYICI ---")
    
    # Ornek: Akdeniz Verileri (Sıcak ve Tuzlu)
    t = 15   # Celcius
    s = 38   # ppt (Tuzluluk)
    d = 200  # Metre (Derinlik)

    speed = calculate_soundspeed(t, s, d)
    
    print(f"Sicaklik: {t} C")
    print(f"Tuzluluk: {s} ppt")
    print(f"Derinlik: {d} m")
    print("-" * 30)
    print(f"SU ALTI SES HIZI: {speed:.2f} m/s")
