from datetime import datetime, timezone
from typing import Self
from uuid import UUID, uuid4

from beanie import Document
from pydantic import Field

from schemas.comment import CommentCreateDto
from schemas.author import Author


class Comment(Document):
    id: UUID = Field(default_factory=uuid4)
    post_id: UUID
    text: str
    author: Author
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @classmethod
    async def create_new(cls, *, dto: CommentCreateDto) -> Self:
        return await cls(post_id=dto.post_id, text=dto.text, author=dto.author).insert()

    class Settings:
        name = 'comments'
        use_state_management = True
