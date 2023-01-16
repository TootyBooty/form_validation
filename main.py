from fastapi import FastAPI, Depends, Body
from fastapi import Request

from depends import get_forms_repository
from repositories.forms import FormsRepository
from validation import validate_dict_values


app = FastAPI(root_path='',
    title='form_validation'
)



@app.on_event("startup")
async def startup():
    forms = get_forms_repository()
    await forms.entry()
    


@app.get('/live/')
async def live():
    return {'Success': True}


@app.get('/form_list/')
async def get(forms: FormsRepository = Depends(get_forms_repository)):
    return await forms.get()


@app.post('/get_form/')
async def get_form(req: Request,
                form_data:dict[str, str] | None = Body(default=None),
                forms: FormsRepository = Depends(get_forms_repository)):
    if not form_data:
        form_data = dict(req.query_params)
    validated_form = await validate_dict_values(form_data)   
    searched_form = await forms.find(validated_form)
    return searched_form if searched_form else validated_form
