from beanie import Document
from pymongo.client_session import ClientSession
from abc import ABC

class BaseStorage(ABC):
    document: Document | None = None

    def __init__(
            self,
            session: ClientSession = None) -> None:
        self.session = session
