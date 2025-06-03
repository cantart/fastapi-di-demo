import uvicorn
from dependency_injector.containers import DeclarativeContainer
from dotenv import load_dotenv
from fastapi import APIRouter, FastAPI

from app2.app import create_app as create_app2

from .container import Container

load_dotenv()

system_router = APIRouter(tags=["system"])
@system_router.get("/health")
async def health_check():
    """
    Health check endpoint.
    """
    return {"status": "ok"}

@system_router.get("/metrics")
async def metrics():
    """
    Metrics endpoint.
    """
    return {"metrics": "not implemented yet"}

def create_app(container: DeclarativeContainer) -> FastAPI:
    app = FastAPI()
    app.container = container
    app.mount("/app2", create_app2(container))
    app.include_router(system_router)
    return app

if __name__ == "__main__":
    app = create_app(Container())
    uvicorn.run(app, host="0.0.0.0", port=8000)