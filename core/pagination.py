from fastapi import Query
from fastapi_pagination import Page

PaginatedPage = Page.with_custom_options(
    size=Query(10, description='Pagination page size', ge=1),
    page=Query(1, description='Pagination page number', ge=1),
)
