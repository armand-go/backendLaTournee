from typing import List
from app.domain.entities import Data

from load_data import load_data


class Core:
    db: List[Data]

    def __init__(self) -> None:
        self.db = self.setup_db()

    def setup_db(self) -> List[Data]:
        data_list = load_data("store.json")
        return [
            Data(
                sku=dat["sku"],
                brand=dat["brand"],
                packing=dat["packing"],
                deposit=dat["deposit"],
                preparation_in_crate=dat["preparation_in_crate"],
            )
            for dat in data_list
        ]
