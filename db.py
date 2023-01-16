from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
from config import MONGODB_URL

# Клиент Mongo DB
client = AsyncIOMotorClient(MONGODB_URL)

# БД form_database
forms_db = client.form_database

# Коллекция forms
forms_collection = forms_db.forms