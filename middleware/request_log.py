from fastapi import Request, Response
from starlette.background import BackgroundTask
from starlette.middleware.base import BaseHTTPMiddleware

from core.logger import logger


def write_log_data(request: Request, response: Response):
    extra = {
        'host': request.headers.get('host'),
        'user-agent': request.headers.get('user-agent'),
        'method': request.method,
        'path': request.url.path,
        'query_params': str(request.query_params),
        'status_code': response.status_code,
    }

    logger.info(request.method + ' ' + request.url.path, extra=extra)


class RequestLogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.background = BackgroundTask(write_log_data, request, response)
        return response
