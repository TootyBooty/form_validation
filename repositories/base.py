class BaseRepository:
    def __init__(self, collection):
        self.collection = collection

    async def drop_collection(self):
        await self.collection.drop()