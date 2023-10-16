from .usecases import Usecase
from app.routes import data as data_ep


class Endpoints:
    usecases: Usecase

    def __init__(self, usecases: Usecase) -> None:
        self.usecases = usecases

        self.data = data_ep.Data(data_usecases=self.usecases.data)
