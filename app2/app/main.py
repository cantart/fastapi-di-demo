import uvicorn
from dependency_injector.containers import DeclarativeContainer
from dotenv import load_dotenv
from fastapi import FastAPI

from .container import Container
from .endpoints import router

load_dotenv()

def create_app(container: DeclarativeContainer) -> FastAPI:
    print("Creating App 2")
    app = FastAPI()
    app.container = container
    app.include_router(router)
    return app

if __name__ == "__main__":
    container = Container()
    app = create_app(container)
    uvicorn.run(app, host="0.0.0.0", port=8002)
