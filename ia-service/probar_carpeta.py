import json
import sys
from pathlib import Path

import numpy as np
import tensorflow as tf
from PIL import Image, ImageOps

BASE = Path(__file__).parent
cfg = json.loads((BASE / "modelos" / "config_modelo.json").read_text(encoding="utf-8"))
modelo = tf.keras.models.load_model(str(BASE / "modelos" / "modelo_botellas.keras"))


def zona(p):
    if p >= cfg["umbral_botella"]:
        return "botella_plastica"
    if p <= cfg["umbral_no_botella"]:
        return "no_botella"
    return "indeterminado"


carpeta = Path(sys.argv[1]) if len(sys.argv) > 1 else BASE / "fotos_prueba"
conteo = {"ok": 0, "indeterminado": 0, "error": 0}

for f in sorted(carpeta.rglob("*")):
    if f.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
        continue
    real = f.parent.name
    img = ImageOps.exif_transpose(Image.open(f)).convert("RGB").resize((224, 224), Image.BILINEAR)
    x = np.expand_dims(np.array(img, dtype="float32"), axis=0)
    p = float(modelo.predict(x, verbose=0)[0][0])
    z = zona(p)
    clave = "indeterminado" if z == "indeterminado" else ("ok" if z == real else "error")
    conteo[clave] += 1
    print(f"{real:18s} {f.name:30s} p={p:.3f} -> {z:18s} [{clave}]")

print(conteo)