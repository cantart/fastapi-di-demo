
from abc import ABC, abstractmethod

from pydantic import BaseModel


class CreateOrderResponse(BaseModel):
    order_id: str
    status: str


class OrderService(ABC):
    @abstractmethod
    def create_order(self, order_id: str) -> CreateOrderResponse:
        pass