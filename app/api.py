from fastapi import APIRouter

from ._dependencies import Core, Endpoints, Store, Usecase, Managers


class API:
    serve = APIRouter()

    def __init__(self, *args) -> None:
        for route in args:
            self.serve.include_router(route.ep)


class LaTourneeAPI:
    core = Core()
    manager = Managers()
    store = Store(core=core)
    usecase = Usecase(store=store, manager=manager)
    endpoints = Endpoints(usecases=usecase)

    router = API(endpoints.data, endpoints.orders)
