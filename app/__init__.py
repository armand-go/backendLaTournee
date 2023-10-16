from fastapi import FastAPI

from .api import LaTourneeAPI

serve = FastAPI(title="La Tournée API", version="1")


@serve.get("/")
def ping():
    return "."


la_tournee_route = LaTourneeAPI().router.serve
serve.include_router(la_tournee_route)
