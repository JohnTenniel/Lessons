# from jinja2 import Template

# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17300},
#     {'model': 'Renault', 'price': 44300},
#     {'model': 'Wolksvagen', 'price': 21300}
# ]
#
# # tpl = "Сумма {{ cs|sum('price') }}"
# # tpl = "Сумма {{ cs|max(attribute = 'price') }}"
# # tpl = "Сумма {{ (cs|min(attribute = 'price')).model }}"
# # tpl = "Сумма {{ cs|random }}"
# tpl = "Сумма {{ cs|replace('model', 'brand') }}"
#
# tm = Template(tpl)
# msg = tm.render(cs=cars)
#
# print(msg)

# Макроопределения

from jinja2 import Template
html = """
{% macro input_func(name, value, type="text", size=40) %}
    <input type="{{ type }}" name="{{ name }}" value="{{ value }}" size="{{ size }}">

{% endmacro%}

<p>{{ input_func('name', 'Введите имя') }}</p>
<p>{{ input_func('psw','Пароль') }}</p>
<p>{{ input_func('email', 'Электронная почта') }}</p>
"""


tm = Template(html)
msg = tm.render(cs=html)

print(msg)
# from jinja2 import Environment, FileSystemLoader
#
# persons = [
#     {"name": "Алексей", "year": 18, "weight": 78.5},
#     {"name": "Никита", "year": 28, "weight": 82.3},
#     {"name": "Виталий", "year": 33, "weight": 94.0}
# ]
#
# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('add_cource.html')
# msg = tm.render(users=persons, title='About Jinja')
#
# print(msg)

#Фреймверки начало
#Flask и Django
