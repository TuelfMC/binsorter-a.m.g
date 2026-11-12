import sys
import numpy as np
import tensorflow as tf
from PIL import Image, ImageOps

modelo = tf.keras.models.load_model("modelos/modelo_botellas.keras")

img = Image.open(sys.argv[1])
img = ImageOps.exif_transpose(img).convert("RGB")
img = img.resize((224, 224), Image.BILINEAR)
x = np.expand_dims(np.array(img, dtype="float32"), axis=0)

print("Probabilidad de botella plastica:", float(modelo.predict(x)[0][0]))