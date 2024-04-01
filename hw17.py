import re


def valid_pass(pas):
    if len(pas) < 6 or len(pas) > 18:
        return "Пароль не соответствует"
    elif pas == "".join(re.findall("[A-Za-z0-9@_-]", pas)):
        return "Пароль соответствует"
    else:
        return "Пароль не соответствует"


print(valid_pass('my-p@ssword'))

# Ветвление для вывода соответствия пароля на каждом этапе.
