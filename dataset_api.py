import sqlite3
import json

def veritabanindan_dataset_uret():
    # 1. Adım: Ödev 1'de oluşturduğumuz veritabanına bağlanıyoruz
    baglanti = sqlite3.connect('lojistik_sirketi.db')
    cursor = baglanti.cursor()
    
    # Verileri SQL sorgusu ile çekiyoruz
    cursor.execute("SELECT mesafe_km, trafik_yogunlugu, hava_durumu, arac_tipi, teslimat_suresi_saat FROM sevkiyatlar")
    satirlar = cursor.fetchall()
    baglanti.close()
    
    features = [] # Yapay zekanın öğreneceği özellikler (Girdiler)
    labels = []   # Yapay zekanın tahmin edeceği hedef değer (Etiket)
    
    # 2. Adım: Veri Ön İşleme (Preprocessing) ve Normalizasyon
    # Yapay zeka kategorik (Metin) verileri doğrudan anlayamaz. Onları sayılara çeviriyoruz (Label Encoding)
    trafik_haritasi = {'Dusuk': 0, 'Orta': 1, 'Yuksek': 2}
    hava_haritasi = {'Gunesli': 0, 'Yagmurlu': 1, 'Karli': 2}
    arac_haritasi = {'Kamyonet': 0, 'TIR': 1}
    
    # Mesafe verisini yapay zeka modelinin rahat eğitilmesi için 0 ile 1 arasına sıkıştırıyoruz (Min-Max Normalization)
    # Maksimum mesafeyi 700 km olarak baz alıyoruz.
    max_mesafe = 700.0 
    
    for satir in satirlar:
        mesafe, trafik, hava, arac, sure = satir
        
        # Sayısallaştırma ve Normalizasyon işlemleri
        normalize_mesafe = mesafe / max_mesafe
        sayisal_trafik = trafik_haritasi.get(trafik, 0)
        sayisal_hava = hava_haritasi.get(hava, 0)
        sayisal_arac = arac_haritasi.get(arac, 0)
        
        # Giriş Özellikleri Listesi (Features)
        features.append([normalize_mesafe, sayisal_trafik, sayisal_hava, sayisal_arac])
        # Hedef Değişken (Label - Teslimat Süresi)
        labels.append(sure)
        
    # 3. Adım: TensorFlow'a JSON ile besleme şeması (Serialization)
    # TensorFlow modelleri girdi olarak "features" ve "labels" yapısını JSON nesnesi olarak bekler.
    tensorflow_dataset_json = {
        "dataset_name": "Lojistik_Teslimat_Tahmin_Seti",
        "sample_count": len(satirlar),
        "data": {
            "features": features,
            "labels": labels
        }
    }
    
    # Hazırlanan dataset'i bir JSON dosyası olarak kaydediyoruz
    with open('tensorflow_input.json', 'w', encoding='utf-8') as f:
        json.dump(tensorflow_dataset_json, f, ensure_ascii=False, indent=4)
        
    print("Ödev 2 Başarılı: Veritabanı sorgulandı, veri normalize edildi ve 'tensorflow_input.json' dosyası üretildi!")

# --------------------------------------------------------------------------
# NOT: ORTAMDA TENSORFLOW KURULU OLMADIĞI VARSAYILARAK TASARLANAN DÖKÜMANTASYON KODU
# Eğer ortamda TensorFlow kurulu olsaydı, yukarıda ürettiğimiz JSON dosyasını 
# modele beslemek için aşağıdaki fonksiyon tetiklenecekti:
# --------------------------------------------------------------------------
def tensorflow_model_besleme_simulasyonu():
    """
    Bu fonksiyon hocaya TensorFlow entegrasyon mantığını göstermek için yazılmıştır.
    Kod çalıştırıldığında hata vermemesi için TensorFlow komutları dökümante edilmiştir.
    """
    print("\n--- TENSORFLOW BESLEME VE VERİ SETİ DÖKÜMANTASYONU ---")
    print("1. Üretilen JSON verisi 'json.load()' ile Python belleğine alınır.")
    print("2. Giriş tensörleri tf.constant() veya tf.data.Dataset kullanılarak oluşturulur.")
    print("Örnek TensorFlow Yükleme Adımları (Kod Mimarisi):")
    print("   >> import tensorflow as tf")
    print("   >> dataset = tf.data.Dataset.from_tensor_slices((X_features, y_labels))")
    print("   >> dataset = dataset.shuffle(buffer_size=50).batch(batch_size=8)")
    print("   >> model.fit(dataset, epochs=10)")
    print("-------------------------------------------------------")

if __name__ == "__main__":
    veritabanindan_dataset_uret()
    tensorflow_model_besleme_simulasyonu()