import sqlite3
#
# country_list = [
#     ('Китай', 1425887337),
#     ('Индия', 1417173173),
#     ('Соединённые Штаты Америки', 338289857),
#     ('Индонезия', 275501339),
#     ('Пакистан', 235824862),
#     ('Нигерия', 218541212),
#     ('Бразилия', 215313498),
#     ('Бангладеш', 171186372),
#     ('Россия', 144713314),
#     ('Мексика', 127504125),
#     ('Япония', 123951692)
# ]
#
# with sqlite3.connect("census.db") as cen:
#     cur = cen.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS countries(
#         country_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         country TEXT,
#         population INTEGER
#     )
#     """)
#     cur.executemany("INSERT INTO countries VALUES(NULL, ?, ?)", country_list)
#     # cur.execute("INSERT INTO countries VALUES(1, 'The whole world', 7975105000)")


with sqlite3.connect("census.db") as cen:
    cen.row_factory = sqlite3.Row
    cur = cen.cursor()
    cur.executescript("""
    CREATE TABLE IF NOT EXISTS countries(
        country_id INTEGER PRIMARY KEY AUTOINCREMENT,
        country TEXT,
        population INTEGER
    );
    CREATE TABLE IF NOT EXISTS new_countries(
        country TEXT, position INTEGER, population INTEGER
    );
    """)

    cur.execute("INSERT INTO countries VALUES(NULL, 'Эфиопия', 123379924)")
    last_row_id = cur.lastrowid
    population = 123379924
    cur.execute("INSERT INTO new_countries VALUES('Эфиопия', ?, ?)", (last_row_id, population))

