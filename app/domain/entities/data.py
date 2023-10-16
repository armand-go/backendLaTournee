from pydantic import BaseModel


class Data(BaseModel):
    sku: str
    brand: str
    packing: int
    deposit: float
    preparation_in_crate: bool
