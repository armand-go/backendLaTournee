from typing import List

from app.adapters import stores, managers

from app.domain import entities
from app.domain.errors import ErrNotFound, ErrUnexpected


class Orders:
    def __init__(self, data_store: stores.Data, manager: managers.Orders) -> None:
        self.__store = data_store
        self.__manager = manager

    async def dispatch_order(self, product_list: List[entities.Product]) -> entities.Dispatch:
        current_dispatch = entities.Dispatch()
        big_slot_remaining = 0
        small_slot_remaining = 0

        for product in product_list:
            try:
                pproduct = await self.__store.get(product.sku)
            except ErrNotFound as e:
                raise e
            except Exception:
                raise ErrUnexpected()

            try:
                (
                    dispatch_for_product,
                    big_slot_remaining,
                    small_slot_remaining,
                ) = await self.__manager.compute_crates_required(
                    pproduct,
                    product.unit_count,
                    old_big_slot_remaining=big_slot_remaining,
                    old_small_slot_remaining=small_slot_remaining,
                )
            except Exception:
                raise ErrUnexpected()

            for key, value in dispatch_for_product.items():
                setattr(current_dispatch, key, getattr(current_dispatch, key) + value)

        return current_dispatch
