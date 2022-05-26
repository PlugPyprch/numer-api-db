from fastapi import FastAPI
import app.models
from app.routes import router
from app.config import engine

app.models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/equa", tags=["equa"])


