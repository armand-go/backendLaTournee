from .core import Core

from app.adapters import stores


class Store:
    core: Core

    data: stores.Data

    def __init__(self, core: Core) -> None:
        self.data = stores.Data(db=core.db)
