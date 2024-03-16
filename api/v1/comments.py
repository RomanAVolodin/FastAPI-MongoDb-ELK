import logging
from uuid import UUID

from fastapi import APIRouter, status, HTTPException
from fastapi_pagination.ext.beanie import paginate

from core.pagination import PaginatedPage
from models import Post
from models.comment import Comment
from schemas.comment import CommentCreateDto, CommentResponse

router = APIRouter(prefix='/comments', tags=['Comments'])

logger = logging.getLogger().getChild('comments-router')


@router.post('', response_model=CommentResponse, status_code=status.HTTP_201_CREATED)
async def _add_comment(dto: CommentCreateDto) -> Comment:
    post = await Post.get_by_id(id=dto.post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Post with ID {dto.post_id} not found',
        )
    comment = await Comment.create_new(dto=dto)
    return comment


@router.get(
    '/{id}',
    summary='Get a list of comments for post',
    response_model=PaginatedPage[CommentResponse],
    status_code=status.HTTP_200_OK,
)
async def _get_all_orders(id: UUID) -> PaginatedPage[Comment]:
    items = await paginate(Comment.find(Comment.post_id == id))
    return items
