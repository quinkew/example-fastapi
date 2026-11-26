from fastapi import FastAPI
from .routers import main_router
from . import models
from .database import engine
from .core.middleware import setup_middlewares

app = FastAPI(title='Social Media')

app.include_router(main_router)
setup_middlewares(app)

# models.Base.metadata.create_all(bind=engine) в случае если alembic не будет работать
