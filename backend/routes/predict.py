from fastapi import APIRouter
from pydantic import BaseModel
from services.model_service import predict_exoplanet

router = APIRouter()

# Definir el esquema de entrada usando Pydantic
class ExoplanetData(BaseModel):
    sy_pnum: int
    pl_orbper: float
    pl_orbperlim: float
    pl_rade: float
    pl_radelim: float
    pl_radj: float
    pl_radjlim: float
    st_rad: float
    sy_dist: float
    sy_vmag: float
    sy_kmag: float
    sy_gaiamag: float
    orbpos: float
    orbneg: float
    radepos: float
    radjpos: float   
    radpos: float    
    radneg: float
    distpos: float
    vmagpos: float
    vmagneg: float
    kmagpos: float
    kmagneg: float
    gaiamagpos: float
    gaiamagneg: float

@router.post("/predict")
async def predict(data: ExoplanetData):
    # Convertimos el modelo Pydantic a dict
    prediction = predict_exoplanet(data.dict())
    return {"prediction": prediction}
