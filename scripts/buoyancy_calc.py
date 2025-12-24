"""
Denizalti Akademisi - Taktik Muhendislik Araclari
Buoyancy & Ballast Calculator v1.0
"""

def calculate_buoyancy(volume, density_water):
    """
    Arsimet prensibine gore kaldirma kuvvetini hesaplar.
    F_buoyancy = Volume * Density * Gravity
    """
    GRAVITY = 9.81
    return volume * density_water * GRAVITY

def calculate_required_ballast(hull_volume, constant_mass, water_density):
    """
    Denizaltinin sehpada (neutral buoyancy) kalmasi icin gereken balast suyunu hesaplar.
    Total Mass = Displacement
    (Constant Mass + Ballast Mass) = Hull Volume * Water Density
    """
    total_displacement_mass = hull_volume * water_density
    required_ballast = total_displacement_mass - constant_mass
    return required_ballast

if __name__ == "__main__":
    print("--- SUBSIM: MUHENDISLIK HESAPLAYICI ---")
    
    # Ornek Veriler
    hull_vol = 3500  # m^3
    ship_mass = 3200 # Ton
    salt_water_density = 1025 # kg/m^3 (Deniz suyu)

    ballast_needed = calculate_required_ballast(hull_vol, ship_mass * 1000, salt_water_density)
    
    print(f"Govde Hacmi: {hull_vol} m^3")
    print(f"Sabit Kutle: {ship_mass} Ton")
    print(f"Su Yogunlugu: {salt_water_density} kg/m^3")
    print("-" * 30)
    print(f"GEREKEN BALAST SUYU: {ballast_needed / 1000:.2f} Ton")
