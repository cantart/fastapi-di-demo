from app.services.order_service.order_service import (CreateOrderResponse,
                                                      OrderService)


class HttpOrderService(OrderService):
    def create_order(self, order_id: str):
        print(f"Creating order via HTTP with ID: {order_id}")
        return CreateOrderResponse(order_id=order_id, status="created")