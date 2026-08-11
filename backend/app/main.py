from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="NovaHIS API",
    version="0.1.0",
    description="Hospital Information System foundation",
)

app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok", "service": "NovaHIS API"}
