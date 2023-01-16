import requests

from repositories.forms import forms_list

def check_forms():
    r = requests.get('http://0.0.0.0:8000/form_list/')
    return r.json()

assert check_forms() == forms_list


def get_form(params:dict):
    p = params
    r = requests.post('http://0.0.0.0:8000/get_form/', params=p)
    return r.json()

# login_form_structure:
# {'name': 'login_form', 'login': 'email', 'password': 'text'}

# successful validation
base_login_form = {'login': 'abc123@car.go', 'password': 'qwerty123'}
login_form_with_add_fields = {'login': 'abc123@car.go', 'password': 'qwerty123', 'foo': 'bar', 'date': '10.10.1010'}
login_form_with_mixed_fields = {'foo': 'bar', 'password': 'qwerty123', 'date': '10.10.1010', 'login': 'abc123@car.go'}

# unsuccessful validation
login_form_without_required_field = {'login': 'abc123@car.go', 'foo': 'bar'}
login_form_with_the_wrong_types = {'login': '+7 123 123 12 12', 'password': '31.12.2022'}

assert get_form(base_login_form)                    == 'login_form'
assert get_form(login_form_with_add_fields)         == 'login_form'
assert get_form(login_form_with_mixed_fields)       == 'login_form'

assert get_form(login_form_without_required_field) != 'login_form'
print(get_form(login_form_without_required_field), end='\n\n')

assert get_form(login_form_with_the_wrong_types)    != 'login_form'
print(get_form(login_form_with_the_wrong_types), end='\n\n')


custom_form = {
    'name': 'Kirill',                   # text
    'mail': 'qwerty2123@mail.ru',       # email
    'bad_mail_1': 'qwerty@@mail.ru',    # text
    'bad_mail_2': 'qwertymail.ru',      # text
    'bad_mail_3': 'qwerty@mailru',      # text
    'phone': '+7 777 777 77 77',        # phone
    'bad_phone_1': '8 777 777 77 77',   # text
    'bad_phone_2': '+7-777-777-77-77',  # text
    'date_1': '10.10.2004',             # date
    'date_2': '2004-10-10',             # date
    'bad_date_1': '2004.10.10',         # text
    'bad_date_2': '10-10-2004',         # text
}

print(get_form(custom_form))