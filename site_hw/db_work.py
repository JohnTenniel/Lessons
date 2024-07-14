import sqlite3



class DataBaseWork:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения из БД")
        return []

    def add_course(self, title,  price,  text):
        try:
            self.__cur.execute("INSERT INTO course VALUES(NULL, ?, ?, ?)", (title, price, text))
            self.__db.commit()
            return True
        except sqlite3.Error as e:
            print("Ошибка добавления курса в БД" + str(e))
            return False

    def get_course(self, course_id):
        try:
            self.__cur.execute(f"SELECT title, price ,text FROM course WHERE id={course_id}")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения описания из БД" + str(e))
            return False
        return False, False

    def get_course_annonce(self):
        try:
            self.__cur.execute("SELECT id, title, price, text FROM course")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения списка курсов из БД" + str(e))
        return []
