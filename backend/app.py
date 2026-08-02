from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes.run_simulation import router as simulation_router

app = FastAPI(title="MMA Money Matrix API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Expose simulation router under /api
app.include_router(simulation_router, prefix="/api")


@app.get("/")
def read_root():
    return {"status": "ok"}
