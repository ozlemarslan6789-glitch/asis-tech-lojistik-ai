import sqlite3

# Veritabanına bağlan
baglanti = sqlite3.connect('lojistik_sirketi.db')
cursor = baglanti.cursor()

# Tabloyu oluştur (SQL içindeki yorum satırlarını sildim, hata vermemesi için)
cursor.execute('''
CREATE TABLE IF NOT EXISTS sevkiyatlar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mesafe_km REAL,
    trafik_yogunlugu TEXT,
    hava_durumu TEXT,
    arac_tipi TEXT,
    teslimat_suresi_saat REAL
)
''')

# 51 adet örnek veri
veri_listesi = [
    (120, 'Dusuk', 'Gunesli', 'Kamyonet', 2.0), (450, 'Yuksek', 'Yagmurlu', 'TIR', 8.5),
    (300, 'Orta', 'Gunesli', 'TIR', 5.0), (80, 'Yuksek', 'Gunesli', 'Kamyonet', 2.5),
    (600, 'Dusuk', 'Karli', 'TIR', 12.0), (210, 'Orta', 'Yagmurlu', 'Kamyonet', 4.0),
    (150, 'Dusuk', 'Gunesli', 'Kamyonet', 2.2), (500, 'Yuksek', 'Karli', 'TIR', 11.5),
    (350, 'Orta', 'Gunesli', 'TIR', 5.5), (95, 'Yuksek', 'Yagmurlu', 'Kamyonet', 3.0),
    (700, 'Dusuk', 'Gunesli', 'TIR', 9.0), (130, 'Orta', 'Karli', 'Kamyonet', 3.5),
    (250, 'Yuksek', 'Gunesli', 'TIR', 4.8), (400, 'Dusuk', 'Yagmurlu', 'TIR', 6.5),
    (180, 'Orta', 'Gunesli', 'Kamyonet', 3.0), (50, 'Yuksek', 'Gunesli', 'Kamyonet', 1.8),
    (620, 'Yuksek', 'Yagmurlu', 'TIR', 10.5), (290, 'Dusuk', 'Gunesli', 'TIR', 4.0),
    (110, 'Orta', 'Yagmurlu', 'Kamyonet', 2.8), (480, 'Orta', 'Karli', 'TIR', 9.5),
    (140, 'Dusuk', 'Gunesli', 'Kamyonet', 2.1), (310, 'Yuksek', 'Gunesli', 'TIR', 5.8),
    (90, 'Orta', 'Karli', 'Kamyonet', 2.9), (530, 'Dusuk', 'Yagmurlu', 'TIR', 8.0),
    (220, 'Yuksek', 'Gunesli', 'Kamyonet', 4.2), (75, 'Dusuk', 'Gunesli', 'Kamyonet', 1.5),
    (650, 'Yuksek', 'Karli', 'TIR', 14.0), (380, 'Orta', 'Yagmurlu', 'TIR', 6.8),
    (160, 'Yuksek', 'Gunesli', 'Kamyonet', 3.4), (420, 'Dusuk', 'Gunesli', 'TIR', 5.5),
    (240, 'Orta', 'Karli', 'Kamyonet', 5.0), (105, 'Yuksek', 'Yagmurlu', 'Kamyonet', 3.1),
    (580, 'Orta', 'Gunesli', 'TIR', 8.2), (135, 'Dusuk', 'Yagmurlu', 'Kamyonet', 2.5),
    (460, 'Yuksek', 'Gunesli', 'TIR', 7.5), (190, 'Orta', 'Gunesli', 'Kamyonet', 3.2),
    (85, 'Dusuk', 'Karli', 'Kamyonet', 2.2), (610, 'Yuksek', 'Gunesli', 'TIR', 9.8),
    (270, 'Dusuk', 'Yagmurlu', 'TIR', 4.5), (115, 'Yuksek', 'Gunesli', 'Kamyonet', 2.7),
    (490, 'Orta', 'Karli', 'TIR', 10.0), (125, 'Dusuk', 'Gunesli', 'Kamyonet', 2.0),
    (330, 'Yuksek', 'Yagmurlu', 'TIR', 6.2), (95, 'Orta', 'Gunesli', 'Kamyonet', 2.1),
    (550, 'Dusuk', 'Karli', 'TIR', 10.5), (230, 'Yuksek', 'Gunesli', 'Kamyonet', 4.5),
    (70, 'Dusuk', 'Yagmurlu', 'Kamyonet', 1.7), (670, 'Yuksek', 'Yagmurlu', 'TIR', 11.8),
    (360, 'Orta', 'Gunesli', 'TIR', 5.2), (170, 'Yuksek', 'Karli', 'Kamyonet', 4.5),
    (510, 'Dusuk', 'Gunesli', 'TIR', 6.8)
]

# Verileri ekle
cursor.executemany('INSERT INTO sevkiyatlar (mesafe_km, trafik_yogunlugu, hava_durumu, arac_tipi, teslimat_suresi_saat) VALUES (?, ?, ?, ?, ?)', veri_listesi)

baglanti.commit()
baglanti.close()
print("Odev 1 Basarili: Lojistik veritabani olusturuldu!")