from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from app.domain import usecases, entities


class Payload:
    class Product(BaseModel):
        ID: str
        OrderID: str
        SKU: str
        UnitCount: int

        def to_entity(self) -> entities.Product:
            return entities.Product(
                id=self.ID, order_id=self.OrderID, sku=self.SKU, unit_count=self.UnitCount
            )

    class Orders(BaseModel):
        Supplier: int
        Slot6: int
        Slot12: int
        Slot20: int

        def from_entity(data: entities.Dispatch) -> "Payload.Orders":
            return Payload.Orders(
                Supplier=data.supplier, Slot6=data.slot_6, Slot12=data.slot_12, Slot20=data.slot_20
            )


class Orders:
    ep = APIRouter(prefix="/orders")
    __uc: usecases.Orders

    def __init__(self, orders_usecases: usecases.Orders) -> None:
        Orders.__uc = orders_usecases

    @staticmethod
    @ep.post("/dispatch", response_model=Payload.Orders)
    async def dispatch_order(product_list: List[Payload.Product]) -> Payload.Orders:
        return Payload.Orders.from_entity(
            await Orders.__uc.dispatch_order([p.to_entity() for p in product_list])
        )
