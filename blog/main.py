from fastapi import FastAPI
from .database import engine
from . import models
from .routers import user,auth,blog

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)

