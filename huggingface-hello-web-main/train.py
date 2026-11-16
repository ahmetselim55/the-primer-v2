import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

# 1. Veriyi Yükle
data_path = "data/oturumlar.csv"
if os.path.exists(data_path):
    df = pd.read_csv(data_path)
    X = df[["seviye", "sure_saniye", "hata_sayisi", "zorluk"]].values.astype('float32')
    y = df["hedef_yardim"].values
else:
    X = [[1.0, 45.0, 2.0, 1.0], [3.0, 12.0, 0.0, 1.0], [2.0, 30.0, 3.0, 2.0], [5.0, 10.0, 0.0, 1.0], [2.0, 60.0, 4.0, 3.0]]
    y = [1, 0, 1, 0, 1]

# 2. Modeli Eğit
model = LogisticRegression(random_state=42)
model.fit(X, y)
print("Model başarıyla eğitildi!")

# 3. ONNX Formatına Dönüştür ve Kaydet
initial_type = [("float_input", FloatTensorType([None, 4]))]
onnx_model = convert_sklearn(model, initial_types=initial_type)

# Çıktıyı model klasörüne kaydedelim
os.makedirs("model", exist_ok=True)
with open("model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

print("model.onnx başarıyla oluşturuldu ve paketlendi!")