from typing import Annotated

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app2.app.container import Container
from app2.app.services import OrderService

router = APIRouter()

@router.post("/")
@inject
async def create_order(
    order_id: str, 
    order_service: Annotated[
        OrderService, Depends(Provide["order_service"])
    ]
):
    """
    Create a new order.
    """
    response = order_service.create_order(order_id)
    return {"order_id": response.order_id, "status": response.status}

@router.get("/aws")
@inject
async def get_aws_config(
    api_key: str = Depends(Provide["config.aws.access_key_id"])
):
    """
    Get AWS configuration.
    """
    return {"aws_api_key": api_key}

@router.get("/environment")
@inject
async def get_environment(
    environment: str = Depends(Provide["config.environment"])
):
    """
    Get the current environment.
    """
    return {"environment": environment}