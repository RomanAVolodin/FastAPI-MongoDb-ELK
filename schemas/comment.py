from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from schemas.author import Author


class CommentCreateDto(BaseModel):
    post_id: UUID
    text: str
    author: Author


class CommentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True, populate_by_name=True)

    id: UUID = Field(UUID, validation_alias='_id')
    post_id: UUID
    text: str
    created_at: datetime
    author: Author
