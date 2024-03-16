import logging
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse
from fastapi_pagination import add_pagination
from motor.motor_asyncio import AsyncIOMotorClient

from api import setup_routers
from core.config import settings
from db import mongo, init_db
from core.logger import LOGGING, setup_root_logger
from middleware.main import setup_middleware

setup_root_logger()


@asynccontextmanager
async def lifespan(_: FastAPI):
    mongo.mongo_client = AsyncIOMotorClient(str(settings.mongodb_uri))
    await init_db.init(client=mongo.mongo_client)
    yield
    mongo.mongo_client.close()


def create_app():
    application = FastAPI(
        lifespan=lifespan,
        title='Post creator',
        docs_url='/docs',
        openapi_url='/api/openapi.json',
        default_response_class=ORJSONResponse,
        description='Orders Service',
        version='0.1.0',
    )

    setup_routers(application)
    setup_middleware(application)
    add_pagination(application)

    return application


app = create_app()


@app.exception_handler(Exception)
def custom_exception_handler(_: Request, exc: Exception):
    return ORJSONResponse(content={'detail': str(exc)})


@app.get('/')
async def root():
    logging.warning('Hello World')
    return {'message': 'Hello World 🎉'}


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        log_config=LOGGING,
        log_level=settings.log_level,
        reload=True,
    )
