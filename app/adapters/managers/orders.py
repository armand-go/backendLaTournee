import math

from typing import Tuple, Dict
from app.domain import entities


class Orders:
    def __init__(self) -> None:
        pass

    async def compute_crates_required(
        self,
        product: entities.Data,
        unit_count: int,
        old_big_slot_remaining: int = 0,
        old_small_slot_remaining: int = 0,
    ) -> Tuple[Dict, int, int]:
        required_crate = {
            "slot_6": 0,
            "slot_12": 0,
            "slot_20": 0,
            "supplier": 0,
        }

        if product.sku == "orangina-25":
            unit_count = math.ceil(unit_count / 2)
            product.preparation_in_crate = False

        is_la_tournee = product.brand == "La Tournée"
        if is_la_tournee:
            unit_count *= 1.2
            product.preparation_in_crate = False

        if product.preparation_in_crate:
            required_crate["supplier"] += unit_count // product.packing
            ct = unit_count % product.packing
        else:
            ct = unit_count

        container_small = product.deposit == 0.2 and product.preparation_in_crate
        big_slot_remaining = 0
        small_slot_remaining = 0

        if container_small:
            ct -= old_small_slot_remaining

            required_crate["slot_20"] += ct // 20
            required_crate["slot_20"] += 1 if ct % 20 else 0

            small_slot_remaining = 20 - ct % 20
        else:
            ct -= old_big_slot_remaining

            required_crate["slot_12"] += ct // 12
            remain = ct % 12

            if remain > 6:
                required_crate["slot_12"] += 1
                big_slot_remaining = 12 - ct % 12
            elif remain > 0:
                required_crate["slot_6"] += 1
                big_slot_remaining = 6 - ct % 6

        return required_crate, big_slot_remaining, small_slot_remaining
