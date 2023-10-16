from pydantic import BaseModel


class Product(BaseModel):
    id: str
    order_id: str
    sku: str
    unit_count: int


class Dispatch(BaseModel):
    supplier: int = 0
    slot_6: int = 0
    slot_12: int = 0
    slot_20: int = 0
