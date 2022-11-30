from ast import Delete
from dataclasses import dataclass
import sqlite3


class Database:
    dataBase_name = 'Data.db'
    def __init__(self):
        print('its work')
        self.recordall = None
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


if __name__ == "__main__":
    database = Database()
    #database.insert_student('Usman','Ali',28,'First year')      #    firstname    ,   lastname    ,   age   ,   class
    #database.update_student(44,'Waleed Butt','Ijaz Butt',27,'bahreen',35)     #   newid , firstname  ,  lastname , age , class , old_id
    #database.delete_student_data_which_id_is(30)
    data = database.get_students_data()
    print(data)
    pass