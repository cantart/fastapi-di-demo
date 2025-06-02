from dotenv import load_dotenv
from fastapi import FastAPI

from app import endpoints

from .container import Container

load_dotenv()

def create_app() -> FastAPI:
    container = Container()
    app = FastAPI()
    app.container = container
    app.include_router(endpoints.router)
    return app

app = create_app()
