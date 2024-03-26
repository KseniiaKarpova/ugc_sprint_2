from storages import BaseStorage
from services import BaseService
from abc import abstractmethod


class BaseReviewService(BaseService):
    def __init__(self, storage: BaseStorage) -> None:
        self.storage = storage

    @abstractmethod
    async def set_like(self):
        pass
    
    @abstractmethod
    async def set_dislike(self):
        pass

    @abstractmethod
    async def mark_review(self):
        pass


