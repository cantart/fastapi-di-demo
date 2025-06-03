from dependency_injector import containers, providers

from app.services.order_service.func_call_order_service import \
    FunctionCallOrderService
from app.services.order_service.http_order_service import HttpOrderService
from app.services.order_service.order_service import OrderService
from app.settings import Settings


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["app.endpoints"])
    config = providers.Configuration(pydantic_settings=[Settings()])
    order_service: OrderService = providers.Selector(
        config.order_service_type,
        http=providers.Factory(HttpOrderService),
        function_call=providers.Factory(FunctionCallOrderService)
    )
    