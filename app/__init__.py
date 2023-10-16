from fastapi import FastAPI

serve = FastAPI(title="La Tournée API", version="1")


@serve.get("/")
def ping():
    return "."
