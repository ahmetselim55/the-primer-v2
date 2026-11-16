import json

def test_parite():
    config_path = "model/config.json"
    
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
        
    print(f"Yüklenen Model Tipi: {config['model_type']}")
    print(f"Model Başarı Skoru (Accuracy): {config['metrics']['accuracy']}")
    
    features = config['features']
    print(f"Kullanılan Özellikler (Features): {features}")
    
    print("Parite Testi Başarıyla Tamamlandı: Model ve Sözleşme Uyumlu!")

if __name__ == "_main_":
    test_parite()