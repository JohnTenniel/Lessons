import csv
from bs4 import BeautifulSoup
import requests
import re


class Parser:
    html = ""

    def __init__(self, url, data):
        self.url = url
        self.data = data

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        p1 = self.html.find("div", class_='crea-group').find_all('div', class_='drawer drawer-sliding')
        for plugin in p1:
            name = plugin.find('h3').text
            name = re.sub("[^A-Za-zА-Яа-я0-9 -]", "", name).lstrip()
            price = plugin.find('div', class_='drawer-foot crea-foot').find('div', class_='tbox-title crea-price')
            if price is not None:
                price = price.text.strip()
            old_price = plugin.find('div', class_='drawer-foot crea-foot').find('del',
                                                                                class_='crea__discount__original-price')
            if old_price is not None:
                old_price = old_price.text.strip()
                if "," in old_price:
                    old_price = old_price.replace(",", ".")
                else:
                    old_price = old_price
            else:
                old_price = price
            sale = plugin.find('div', class_='drawer-foot crea-foot').find('span')
            if sale is not None:
                sale = sale.text.strip()
                sale_price = float(old_price.split()[0]) - (
                        float(old_price.split()[0]) / 100 * int(sale.strip()[1:3]))
                sale_price = round(sale_price, 2)
                price = sale_price
            else:
                sale = "0%"

            self.data = {
                'Наименование': name,
                'Цена': price,
                "Старая цена": old_price,
                'Скидка': sale
            }
            print(self.data)
            Parser.write_csv(self)

    def write_csv_name(self):
        with open("hw34.csv", "a") as f:
            writer = csv.writer(f, delimiter=";", lineterminator="\r")
            writer.writerow(('Наименование', 'Цена', 'Старая цена', 'Скидка'))

    def write_csv(self):
        with open("hw34.csv", "a") as f:
            writer = csv.writer(f, delimiter=";", lineterminator="\r")
            writer.writerow(
                (self.data['Наименование'], self.data['Цена'], self.data['Старая цена'], self.data['Скидка']))

    def run(self):
        self.write_csv_name()
        self.get_html()
        self.parsing()
        self.write_csv()


