from pathlib import Path

import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API de prédiction Wine")

# Charger le modèle exporté par le TP4
MODEL_PATH = Path(__file__).parent / "modele_final.pkl"
modele = joblib.load(MODEL_PATH)


class DonneesPrediction(BaseModel):
    features: list[float]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(donnees: DonneesPrediction):
    if len(donnees.features) != 13:
        raise HTTPException(
            status_code=400,
            detail="Il faut fournir exactement 13 valeurs numériques."
        )

    prediction = int(modele.predict([donnees.features])[0])
    probabilites = modele.predict_proba([donnees.features])[0]
    confiance = float(max(probabilites))

    return {
        "prediction": prediction,
        "confidence": confiance
    }