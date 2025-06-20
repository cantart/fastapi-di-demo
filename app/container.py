from dependency_injector import containers, providers

from app2.app.services import OrderService
from app2.app.settings import Settings
from app.func_call_order_service import FunctionCallOrderService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["app2.app.endpoints"])
    config = providers.Configuration(pydantic_settings=[Settings()])
    order_service: OrderService = providers.Factory(FunctionCallOrderService)