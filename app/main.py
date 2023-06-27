from fastapi import FastAPI
from config import engine
import models 
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/student", tags=["student"])