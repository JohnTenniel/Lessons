from jinja2 import Template

menu = [
    {'id': '/index', 'pos': 'Главная'},
    {'id': '/news', 'pos': 'Новости'},
    {'id': '/about', 'pos': 'О компании'},
    {'id': '/shop', 'pos': 'Магазин'},
    {'id': '/contacts', 'pos': 'Контакты'}
]

link = """<ul>
{% for m in menu -%}
    {% if m['pos'] == 'Главная' -%}
        <li><a href = "{{ m['id'] }}" class="active">{{ m['pos'] }}</a></li>
    {%- else -%}
        <li><a href = "{{ m['id'] }}">{{ m['pos'] }}</a></li> 
    {%- endif %}   
{% endfor -%}
</ul>
"""

tm = Template(link)
msg = tm.render(menu=menu)

print(msg)
