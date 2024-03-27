from models.review import FilmReview, Document
from storages import BaseStorage
from uuid import UUID
from schemas.author import Author


class ReviewStorage(BaseStorage):
    document: Document = FilmReview

    async def create(self, film_id: UUID, author: Author, mark: int, text: str = None):
        return await FilmReview(
            film_id=film_id,
            mark=mark,
            author=author.model_dump(),
            text=text).create(session=self.session)
