import joblib
import numpy as np
from pathlib import Path

# Ruta al modelo entrenado
MODEL_PATH = Path(__file__).resolve().parent.parent / "gradient_boosting_model.pkl"

# Intentar cargar el modelo al iniciar el servicio
try:
    model = joblib.load(MODEL_PATH)
    print("✅ Modelo cargado correctamente")
except:
    model = None
    print("⚠️ No se encontró model.pkl, se usará predicción simulada")


def predict_exoplanet(data: dict):
    """
    Recibe un diccionario con las 23 columnas
    Lo convierte en un vector numpy en el orden de entrenamiento
    """

    # Orden EXACTO de las columnas usadas en entrenamiento
    features_order = [
        "sy_pnum", "pl_orbper", "pl_orbperlim", "pl_rade", "pl_radelim",
        "pl_radj", "pl_radjlim", "st_rad", "sy_dist", "sy_vmag", "sy_kmag", "sy_gaiamag",
        "orbpos", "orbneg", "radepos", "radjpos", "radpos", "radneg", "distpos",
        "vmagpos", "vmagneg", "kmagpos", "kmagneg", "gaiamagpos", "gaiamagneg"
    ]



    # Construir vector de entrada en el orden correcto
    features = np.array([[float(data.get(col, 0)) for col in features_order]])

    # Si hay modelo entrenado
    if model:
        prediction = model.predict(features)[0]   # salida real
    else:  
        prediction = "simulated_exoplanet_detected"  # salida dummy

    return prediction
