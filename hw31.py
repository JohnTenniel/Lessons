import json

data = {}


class CountryCapital:
    def __init__(self, country, capital):
        self.country = country
        self.capital = capital
        data[self.country] = self.capital

    def __str__(self):
        return f"{self.country}: {self.capital}"

    @staticmethod
    def add_country(filename):
        country_name = input("Введите название страны (с заглавной буквы):")
        capital_name = input("Введите название столицы (с заглавной буквы):")

        try:
            date = json.load(open(filename))
        except FileNotFoundError:
            date = {}

        date[country_name] = capital_name

        with open(filename, "w") as f:
            json.dump(date, f, indent=2)
        print("Файл сохранен")

    @staticmethod
    def load_from_file(filename):
        with open(filename, "r") as f:
            print(json.load(f))

    @staticmethod
    def delete_from_file(filename):
        with open(filename) as f:
            temp = json.load(f)
        delete_key = input("Название страны которую хотите удалить из списка (с заглавной буквы): ")
        if delete_key in temp:
            temp.pop(delete_key)
        else:
            print("Такой страны нет в списке")
        with open(filename, "w") as f:
            json.dump(temp, f, indent=2)
        print("Файл сохранен")

    @staticmethod
    def find_in_file(filename):
        with open(filename) as f:
            temp = json.load(f)
        count = 0
        find_name = input("Введите название искомой страны или столицы (с заглавной буквы):")
        for key, value in temp.items():
            if key == find_name or value == find_name:
                print(f'{key}: {value}')
                count = 1
        if count == 0:
            print("Такой страны или столицы не найдено в списке")

    @staticmethod
    def reload_date(filename):
        reload = input("Введите название страны или столицы которую хотите исправить(с заглавной буквы):")
        count = 0
        with open(filename) as f:
            temp = json.load(f)
        for key, value in temp.items():
            if key == reload:
                name = temp.pop(reload)
                country_name = input("Введите новое название страны (с заглавной буквы):")
                capital_name = name
                temp[country_name] = capital_name
                count = 1
                with open(filename, "w") as f:
                    json.dump(temp, f, indent=2)
            if value == reload:
                temp[key] = input(f"Введите новое название столицы для {temp[key]} (с заглавной буквы):")
                count = 1
        if count == 0:
            print("По запросу ничего не найдено")

        with open(filename, "w") as f:
            json.dump(temp, f, indent=2)
        print("Файл сохранен")


file = 'list_capital.json'
index = ''
while index != '6':
    index = input("*" * 40 + "\nВыбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
                             "4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы\nВвод:")
    if index == '1':
        CountryCapital.add_country(file)
    if index == "2":
        CountryCapital.delete_from_file(file)
    if index == "3":
        CountryCapital.find_in_file(file)
    if index == "4":
        CountryCapital.reload_date(file)
    if index == "5":
        CountryCapital.load_from_file(file)