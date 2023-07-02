from routers import city
from routers import weather
import models.models as models

from fastapi import FastAPI
from database.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(weather.router, tags=['Weather'], prefix='/api/weather')
app.include_router(city.router, tags=['City'], prefix='/api/city')

@app.get("/api/healthcheck")
def root():
    return {"message": "API should be working properly."}
