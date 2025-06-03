from app2.app.services import CreateOrderResponse, OrderService


class FunctionCallOrderService(OrderService):
    def create_order(self, order_id: str):
        print(f"Creating order via function call with ID: {order_id}")
        return CreateOrderResponse(order_id=order_id, status="created")