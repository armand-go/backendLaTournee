from .core import Core

from app.adapters import managers


class Managers:
    core: Core

    orders: managers.Orders

    def __init__(self) -> None:
        self.orders = managers.Orders()
