from fastapi import APIRouter
from pydantic import BaseModel

from app.domain import usecases, entities


class Payload:
    class Data(BaseModel):
        sku: str
        brand: str
        packing: int
        deposit: float
        preparation_in_crate: bool

        def from_entity(data: entities.Data) -> "Payload.Data":
            return Payload.Data(**data.model_dump())


class Data:
    ep = APIRouter(prefix="/data")
    __uc: usecases.Data

    def __init__(self, data_usecases: usecases.Data) -> None:
        Data.__uc = data_usecases

    @staticmethod
    @ep.get("/{id}", response_model=Payload.Data)
    async def get_single_data(id: str) -> Payload.Data:
        return Payload.Data.from_entity(await Data.__uc.retrieve_single_data(id))
