from typing import List

from app.domain import entities
from app.domain.errors import ErrNotFound


class Data:
    def __init__(self, db: List[entities.Data]) -> None:
        self.__db = db

    async def get(self, id: str) -> entities.Data:
        query_iter = filter(lambda x: x.sku == id, self.__db)

        try:
            data = next(query_iter)
        except StopIteration as e:
            print("404 NOT FOUND", e)
            raise ErrNotFound("Data")

        return data
