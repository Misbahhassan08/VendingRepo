import sqlite3

class Database:
    my_data_base = 'DB.db'
    def __init__(self):
        print('Data Base Working.....')
        pass
    def table_login(self):
        try:

            conn = sqlite3.connect(self.my_data_base)
            cursor = conn.cursor()
            cursor.execute("""
                               CREATE TABLE IF NOT EXISTS login
                               (UID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                               username TEXT, 
                               password TEXT )""")
            cursor.execute(""" INSERT INTO login 
                               (username , password)
                           VALUES 
                           (?,?)
                           """, ('username', 'password'))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except:
            print('Data Based Connection Faild.....')
        return False
        pass
    def get_Data(self):
        conn = sqlite3.connect(self.my_data_base)
        cursor = conn.cursor()
        cursor.execute("select * from login")
        record = cursor.fetchall()
        print(record)
        conn.commit()
        cursor.close()
        conn.close()
        return record
        pass


    pass


if __name__ == "__main__":

    database = Database()
    #database.table_login()
    database.get_Data()
    pass