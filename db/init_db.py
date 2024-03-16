from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from core.config import settings
from models import gather_documents


async def init(*, client: AsyncIOMotorClient) -> None:
    await init_beanie(
        database=getattr(client, settings.mongodb_db_name),
        document_models=gather_documents(),  # type: ignore[arg-type]
    )
