import csv
from bs4 import BeautifulSoup
import requests
import re


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open("hw33.csv", "a") as f:
        writer = csv.writer(f, delimiter=";", lineterminator="\r")
        # writer.writerow((data['Наименование'], data['Цена'], data['Скидка'], data['Новая цена']))
        writer.writerow((data['Наименование'], data['Цена'], data['Скидка'], data['Старая цена']))


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    p1 = soup.find("div", class_='crea-group').find_all('div', class_='drawer drawer-sliding')
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
        else:
            sale = "0%"
            sale_price = float(old_price.split()[0]) - (
                    float(old_price.split()[0]) / 100 * int(sale.strip()[1:3]))
            sale_price = round(sale_price, 2)
            if sale_price > 0:
                price = sale_price
            else:
                price = price

            # if sale == "00":
            # #     sale = "0%"          sale_price = float(old_price.split()[0]) - (
            #                 float(old_price.split()[0]) / 100 * int(sale.strip()[1:3]))
            #     sale_price = round(sale_price, 2)
            #     if sale_price > 0:
            #         price = sale_price
            #     else:
            #         price = price
            # else:
            #     sale = "0%"
            # # if sale == "00":
            # #     sale = "0%"

            data = {
                'Наименование': name,
                'Цена': price,
                "Старая цена": old_price,
                'Скидка': sale,
                # 'Новая цена': sale_price

            }
            print(data)
            write_csv(data)


def main():
    url = "https://cults3d.com/ru/kategorii/art?only_featured=true&page=1"
    get_data(get_html(url))


if __name__ == '__main__':
    main()
