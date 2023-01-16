from repositories.forms import FormsRepository
from db import forms_collection


def get_forms_repository() -> FormsRepository:
    return FormsRepository(collection=forms_collection)