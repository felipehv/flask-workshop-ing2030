import sqlite3

class DB:

    def __init__(self):
        self.conn = sqlite3.connect("ing2030.db")
        self.cursor = self.conn.cursor()


    def init_db(self):
        self.cursor.execute("DROP TABLE IF EXISTS Users;")
        self.conn.commit()
        self.cursor.execute("""
            CREATE TABLE Users(id integer primary key autoincrement, name, age);
            """)
        self.conn.commit()
        self.cursor.execute("""
        CREATE TABLE Phones(id integer primary key autoincrement, number, brand, carrier, user_id);
        """)
        
        self.conn.commit()


    def get_all_users(self):
        query = self.cursor.execute("SELECT * FROM Users;")
        return {"users" : [row for row in query] }

    def get_phones_by_user_id(self, id):
        query = self.cursor.execute("""
            SELECT * FROM Phones WHERE user_id = ?;
        """, (id,) )
        return {"phones" : [row for row in query] , "user_id": id}

    def create_phone(self, id, data):
        query = self.cursor.execute('''
        INSERT INTO Phones 
        VALUES (null,?,?,?,?);''', 
        (data['number'], data['brand'], data['carrier'], id))
        
        self.conn.commit()
        return 'ok'

    def get_user_by_id(self, id):
        query = self.cursor.execute("SELECT name,age FROM Users WHERE id=?;", (id,))
        try:
            user = query.fetchone()
            return {
                    "user": 
                        {"name": user[0],
                        "age": user[1]}
                    }

        except:
            return {"error": "User not found"}





    def create_user(self, data):
        self.cursor.execute("INSERT INTO Users VALUES (null,?,?)", (data['name'], int(data['age']))  )
        self.conn.commit()
        return

    def create_notebook(self, user_id, params):
        self.cursor.execute("""
            INSERT INTO Notebooks VALUES(null, ?, ?);
        """, (params['brand'], user_id))
        self.conn.commit()


    def modify_user(self, id, data):
        self.cursor.execute("UPDATE Users SET name=?, age=? WHERE id = ?", (data["name"], data["age"],id))
        self.conn.commit()
        return

    def delete_user(self, id):
        self.cursor.execute("DELETE FROM Users WHERE id=?", (id,) )
        self.conn.commit()
        return "Se ha eliminado el usuario {}".format(id)


if __name__ == "__main__":
    db = DB()
    db.init_db()
    with open("users.csv", "r") as reader:
        for line in reader:
            line = line.split(",")
            db.create_user({'name': line[0], 'age': line[1]})
    db.conn.close()


