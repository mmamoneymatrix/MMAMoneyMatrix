from fastapi import FastAPI
from routes.run_simulation import router as simulation_router

app = FastAPI()

# include routes
app.include_router(simulation_router, prefix="/api")
