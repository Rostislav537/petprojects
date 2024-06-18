import sqlite3
class DbWork:
    def __init__(self):

        self.connection = sqlite3.connect('users.db')
        self.cursor = self.connection.cursor()

        self.cursor.execute('CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY,username TEXT NOT NULL,password TEXT NOT NULL)')
    def AddUser(self, username, password):  #добавлюет нового юзера
        if len(password)<8:     #проверка длинны пароля
            return "Failed, password so short"

        self.cursor.execute('SELECT * FROM Users')
        results = self.cursor.fetchall()
        print(results)
        for user in results:    #проверка есть ли уже юзер
            if username in user:
                print("NOT")
                return "Failed, username is registered"

        self.cursor.execute('INSERT INTO Users (username, password) VALUES (?, ?)',(username, password))
        self.connection.commit()
        return "Success"
    def CheckUser(self, username, password):    #проверка пароля
        try:    #трай ексепт так как если пользователь не находится - выдает ошибку
            self.cursor.execute('SELECT username, password FROM Users WHERE username = ?', (username,))
            results = self.cursor.fetchone()
            print(results)
            if password in results:
                return True
            else:
                return False
        except:
            return "Error, this username not in database"
    def DeleteUser(self, username, password):   #удаление юзера с базы данных
        self.cursor.execute('SELECT * FROM Users')
        results = self.cursor.fetchall()
        for user in results:
            if username in user and password in user:
                self.cursor.execute('DELETE FROM Users WHERE id = ?', (user[0],))
                self.connection.commit()
                return "Success"
        return "Failed, data is incorrect"
    def ViewBase(self):     #возвращает список всех юзеров
        self.cursor.execute('SELECT username, id FROM Users')
        results = self.cursor.fetchall()
        return results
    def CloseDB(self):  #закрывает базу данных
        self.connection.close()
