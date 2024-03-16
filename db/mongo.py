from motor.motor_asyncio import AsyncIOMotorClient


mongo_client: AsyncIOMotorClient | None = None


async def get_mongo_client() -> AsyncIOMotorClient:
    return mongo_client
