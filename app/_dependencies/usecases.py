from .store import Store
from .managers import Managers
from app.domain import usecases


class Usecase:
    store: Store
    manager: Managers

    data: usecases.Data

    def __init__(self, store: Store, manager: Managers) -> None:
        self.store = store
        self.manager = manager

        self.data = usecases.Data(data_store=store.data)
        self.order = usecases.Orders(data_store=store.data, manager=self.manager.orders)
