import asyncio
from passlib.context import CryptContext
from motor.motor_asyncio import AsyncIOMotorClient

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def seed():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["agrisen"]
    hashed = pwd_context.hash("password123")
    user = {
        "name": "Test Farmer",
        "email": "test@example.com",
        "password": hashed,
        "role": "farmer",
        "is_verified": True
    }
    await db["users"].delete_many({"email": "test@example.com"})
    await db["users"].insert_one(user)
    print("Test user created: test@example.com / password123")
    client.close()

if __name__ == "__main__":
    asyncio.run(seed())
