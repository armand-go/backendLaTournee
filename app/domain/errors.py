from http import HTTPStatus

from fastapi import HTTPException


class ErrNotFound(HTTPException):
    """
    ErrUnotFound has to be raised if data was expected but
    not does not exits.
    """

    status = HTTPStatus.NOT_FOUND

    def __init__(self, key: str):
        self.__key = key
        self.__error = "not found"
        super().__init__(status_code=self.status, detail=f"{key.upper()}: {self.__error}")

    def to_json(self) -> dict:
        return {"key": self.__key, "error": self.__error}


class ErrUnexpected(HTTPException):
    """
    ErrUnexpected represents global exception for errors that should not happen
    and we don't wish to provide information to end user.
    """

    status = HTTPStatus.INTERNAL_SERVER_ERROR

    def __init__(self, key: str):
        self.__key = key
        self.__error = "not found"
        super().__init__(status_code=self.status)

    def to_json(self) -> dict:
        return {
            "error": "something unexpected happened",
            "ERROR": "Internal error",
        }
