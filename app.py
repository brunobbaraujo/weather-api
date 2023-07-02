from routers import city
from routers import weather
import models.models as models
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from database.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(weather.router, tags=['Weather'], prefix='/api/weather')
app.include_router(city.router, tags=['City'], prefix='/api/city')

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the API!"}
