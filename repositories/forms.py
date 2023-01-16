from .base import BaseRepository

# Список форм, которые будут добавлены в коллекцию при запуске приложения
forms_list = [
        {'name': 'login_form',
        'login': 'email',
        'password': 'text'},

        {'name': 'order_form',
        'recipient_phone': 'phone',
        'recipient_email': 'email',
        'delivery_date': 'date'},

        {'name': 'sms_form',
        'sender': 'phone',
        'receiver': 'phone',
        'message': 'text'},

        {'name': 'intensive_form',
        'start': 'date',
        'finish': 'date',
        'teacher_mail': 'email',
        'teacher_fullname': 'text'},

        {'name': 'post_form',
        'autor': 'email',
        'created_at': 'date',
        'post_title': 'text',
        'post_text': 'text'},
]

class FormsRepository(BaseRepository):
    async def entry(self):
        'Заполняет коллекцию изначальными формами'
        if await self.collection.count_documents({}) == 0:
            await self.collection.insert_many(forms_list)

    async def get(self):
        "Возвращает список всех форм в коллекции"
        cursor = self.collection.find({}, {'_id': 0})
        res = []
        for doc in await cursor.to_list(length=None):
            res.append(doc)
        return res

    async def find(self, search_form) -> str|None:
        "Получает все формы из коллекции, сравнивает поля с заданной формой и возвращает имя шаблона, если он был найден"
        cursor = self.collection.find({}, {'_id': 0})
        # Преобразования словаря {'foo': bar} в множество вида {('foo', 'bar'), }
        search_form_items = set(search_form.items())
        # Проходим по каждому шаблону и сравниваем является ли он подмножеством заданной формы
        for form in await cursor.to_list(length=None):
            form_name = form.pop('name', 'Unnamed_form')
            form_items = set(form.items())
            if form_items.issubset(search_form_items):
                return form_name
        return None
        