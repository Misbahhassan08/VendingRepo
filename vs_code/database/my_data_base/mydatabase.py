from ast import Delete
from dataclasses import dataclass
import sqlite3


class Database:
    dataBase_name = 'Data.db'
    def __init__(self):
        print('its work')
        self.recordall = None
        pass

    def insert_student(self, firstname, lastname, age, _class):
        try:

            conn = sqlite3.connect(self.dataBase_name)
            cursor = conn.cursor()

            cursor.execute("""
                               CREATE TABLE IF NOT EXISTS student
                               (UID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                               firstname TEXT, 
                               lastname TEXT,
                               age TEXT,
                               _class TEXT )""")

            cursor.execute(""" INSERT INTO student
                               (firstname , lastname, age, _class)
                           VALUES 
                           (?,?,?,?)
                           """, (firstname, lastname, age, _class))

            conn.commit()
            cursor.close()
            conn.close()
            return True
        except:
            print('Error in Data base: Inserting Temp Values')
            return False
        
        pass
    def get_students_data(self):
        try:
            print('In show user database calling')
            db = sqlite3.connect(self.dataBase_name)
            sql = 'SELECT * from student'
            cur = db.cursor()
            cur.execute(sql)
            #db.close()
            while True:
                record = cur.fetchone()
                print(record)
                if record is None:
                    break
            db.close()
        except:
            print('Error in fetching student')
        pass

    def update_student(self,new_id, firstname, lastname, age,_class,old_id):
        print('Updating login person now please wait ....')
        conn = sqlite3.connect(self.dataBase_name)
        cursor = conn.cursor()
        cursor.execute("UPDATE student set UID = ? , firstname = ?, lastname = ?, age = ?, _class = ? WHERE UID = ?",
                       (new_id, firstname, lastname,age,_class,old_id))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Student data updated successfully which id was {old_id} to id = {new_id}")
        return True
        pass
    def delete_student_data_which_id_is(self,id):
        conn = sqlite3.connect(self.dataBase_name)
        cursor = conn.cursor()
        cursor.execute("delete from student where UID = ? ", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Deleted student which id = {id}")
        return True
        pass




if __name__ == "__main__":
    database = Database()
    #database.insert_student('Usman','Ali',28,'First year')      #    firstname    ,   lastname    ,   age   ,   class
    #database.update_student(44,'Waleed Butt','Ijaz Butt',27,'bahreen',35)     #   newid , firstname  ,  lastname , age , class , old_id
    #database.delete_student_data_which_id_is(30)
    data = database.get_students_data()
    print(data)
    pass