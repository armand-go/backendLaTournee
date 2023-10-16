from app.adapters import stores

from app.domain import entities
from app.domain.errors import ErrNotFound, ErrUnexpected


class Data:
    def __init__(self, data_store: stores.Data) -> None:
        self.__store = data_store

    async def retrieve_single_data(self, id: str) -> entities.Data:
        try:
            data = await self.__store.get(id)
        except ErrNotFound as e:
            raise e
        except Exception:
            raise ErrUnexpected()

        return data
