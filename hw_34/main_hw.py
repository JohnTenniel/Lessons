from parser_hw import Parser


def main():
    for i in range(1, 6):
        pars = Parser(f"https://cults3d.com/ru/kategorii/art?only_featured=true&page={i}", "hw34.csv")
        pars.run()


if __name__ == '__main__':
    main()
