from .store import Store
from app.domain import usecases


class Usecase:
    store: Store

    data: usecases.Data

    def __init__(self, store: Store) -> None:
        self.store = store

        self.data = usecases.Data(data_store=store.data)
