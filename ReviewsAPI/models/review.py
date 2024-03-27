from datetime import datetime, timezone
from uuid import UUID, uuid4
from schemas.author import Author
from beanie import Document
from pydantic import Field, BaseModel


class BaseMixin(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class FilmReview(BaseMixin, Document):
    film_id: UUID
    author: Author
    text: str = Field(None)
    mark: int = Field(ge=0, le=10)

    class Settings:
        name = "film_review"
        use_state_management = True


class ReviewMark(BaseMixin, Document):
    review_id: UUID
    mark: int = Field(ge=0, le=10)
    author: Author

    class Settings:
        name = "review_mark"
        use_state_management = True
