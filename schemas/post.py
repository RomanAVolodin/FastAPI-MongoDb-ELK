from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from schemas.author import Author


class PostCreateDto(BaseModel):
    subject: str
    text: str
    author: Author


class Like(BaseModel):
    created_at: datetime
    author: Author


class PostResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True, populate_by_name=True)

    id: UUID = Field(UUID, validation_alias='_id')
    slug: str
    subject: str
    text: str
    is_published: bool
    views: int
    last_visit_at: datetime | None = None
    created_at: datetime
    author: Author
    likes: list[Like] | None = None
