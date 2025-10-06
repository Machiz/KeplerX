from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import predict

app = FastAPI(title="KeplerX API")

# Configurar CORS (para conectar con tu frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en producción, restringir al dominio del frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(predict.router)

@app.get("/")
def root():
    return {"message": "KeplerX API is running 🚀"}
