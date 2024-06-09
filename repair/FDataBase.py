import sqlite3


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def addStatement(self, name, phone_number, comm):
        try:
            self.__cur.execute(
                "INSERT INTO request VALUES(NULL, ?, ?, ?)",
                (name, phone_number, comm,),
            )
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления статьи в БД " + str(e))
            return False

        return True