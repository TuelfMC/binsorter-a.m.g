import io
import json
from contextlib import asynccontextmanager
from pathlib import Path

import numpy as np
import tensorflow as tf
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image, ImageOps, UnidentifiedImageError



BASE = Path(__file__).parent
MAX_BYTES = 5 * 1024 * 1024
MAX_PIXELES = 25_000_000
TIPOS_PERMITIDOS = {"image/jpeg", "image/png", "image/webp"}
estado = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    ruta = BASE / "modelos"
    estado["config"] = json.loads((ruta / "config_modelo.json").read_text(encoding="utf-8"))
    estado["modelo"] = tf.keras.models.load_model(str(ruta / "modelo_botellas.keras"))
    yield
    estado.clear()


app = FastAPI(title="BinSorter IA", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


def preparar(datos: bytes) -> np.ndarray:
    try:
        img = Image.open(io.BytesIO(datos))
        if img.width * img.height > MAX_PIXELES:
            raise HTTPException(422, "La imagen tiene demasiados píxeles.")
        img = ImageOps.exif_transpose(img).convert("RGB")
    except (UnidentifiedImageError, OSError, Image.DecompressionBombError):
        raise HTTPException(422, "El archivo no es una imagen válida.")
    img = img.resize((224, 224), Image.BILINEAR)
    return np.expand_dims(np.array(img, dtype="float32"), axis=0)


def decidir(prob: float, cfg: dict):
    if prob >= cfg["umbral_botella"]:
        return "botella_plastica", prob
    if prob <= cfg["umbral_no_botella"]:
        return "no_botella", 1 - prob
    return "indeterminado", None


@app.get("/health")
def health():
    return {"estado": "ok", "version_modelo": estado["config"]["version_modelo"]}


@app.post("/predict")
def predict(imagen: UploadFile = File(...)):
    if imagen.content_type not in TIPOS_PERMITIDOS:
        raise HTTPException(415, "Formato no admitido. Usa JPG, PNG o WEBP.")
    datos = imagen.file.read(MAX_BYTES + 1)
    if len(datos) > MAX_BYTES:
        raise HTTPException(413, "La imagen supera los 5 MB.")

    x = preparar(datos)
    prob = float(estado["modelo"].predict(x, verbose=0)[0][0])
    resultado, confianza = decidir(prob, estado["config"])
    return {
        "resultado": resultado,
        "confianza": confianza,
        "probabilidad_botella": prob,
        "version_modelo": estado["config"]["version_modelo"],
    }
    
    BASE = Path(__file__).parent
cfg = json.loads((BASE / "modelos" / "config_modelo.json").read_text(encoding="utf-8"))
modelo = tf.keras.models.load_model(str(BASE / "modelos" / "modelo_botellas.keras"))