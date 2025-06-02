from typing import Annotated

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.container import Container
from app.services.order_service.order_service import OrderService

router = APIRouter()

@router.post("/")
@inject
async def create_order(
    order_id: str, 
    order_service: Annotated[
        OrderService, Depends(Provide[Container.order_service])
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
    api_key: str = Depends(Provide[Container.config.aws.access_key_id])
):
    """
    Get AWS configuration.
    """
    return {"aws_api_key": api_key}