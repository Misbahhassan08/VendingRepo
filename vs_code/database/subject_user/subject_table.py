import sqlite3

class Subjec_Data_Base:
    my_db = 'login.db'
    def __init__(self):
        print("My Subjec Data Base Is Working.....")
        pass    # end of __init__ function
    def create_subjec_table(self):
        try:

            conn = sqlite3.connect(self.my_db)
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS subjec
                        (subjectid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        total_marks INTEGER,
                        marks_obtained INTEGER,
                        result TEXT,
                        remarks TEXT)""")
                           
            conn.commit()
            cursor.close()
            conn.close()
            print("Data Base subjec Table Created Successfully....")
        except:
            print("Data Base Connection Failed to create subjec table.....")
            pass    # end of create_login_table function
    
    def insert_in_subjec_table(self,total,obtained,resul,remak):
        try:
            conn = sqlite3.connect(self.my_db)
            cursor = conn.cursor()
            cursor.execute(""" INSERT INTO subjec 
                                    (total_marks , marks_obtained , result , remarks)
                            VALUES 
                            (?,?,?,?)
                            """, (total,obtained,resul,remak))
                            
            conn.commit()
            cursor.close()
            conn.close()
            print("Data Inserted Successfully in subjec Data base....")
        except:
            print("Subjects Data Base Connection Failed.....")
        pass    #end of insert function

    def get_subjectid_from_subjec(self):
        try:

            conn = sqlite3.connect(self.my_db)
            cursor = conn.cursor()
            sql = """SELECT subjectid FROM subjec """
            cursor.execute(sql)
            self.subjectid_subjec = cursor.fetchall()
            return self.subjectid_subjec
        except:
            print("Data Base Connection Failed to get subjec subjectid data.....")
        conn.commit()
        cursor.close()
        conn.close()
        pass    # end of sebjectid data get function   

    def get_total_marks(self):
        try:

            conn = sqlite3.connect(self.my_db)
            cursor = conn.cursor()
            sql = """SELECT total_marks FROM subjec """
            cursor.execute(sql)
            self.total_marks = cursor.fetchall()
            return self.total_marks
        except:
            print("Data Base Connection Failed to get subjec total marks data.....")
        conn.commit()
        cursor.close()
        conn.close()
        pass  # end of show_daat_from_login function

    def get_marks_obtained(self):
        try:

            conn = sqlite3.connect(self.my_db)
            cursor = conn.cursor()
            sql = """SELECT marks_obtained FROM subjec """
            cursor.execute(sql)
            self.marks_obtained = cursor.fetchall()
            return self.marks_obtained
        except:
            print("Data Base Connection Failed to get subjec marks obtained data.....")
        conn.commit()
        cursor.close()
        conn.close()
        pass  # end of get_data_from_login_of_user_id function

    def get_result(self):
        try:

            conn = sqlite3.connect(self.my_db)
            cursor = conn.cursor()
            sql = """SELECT result FROM subjec """
            cursor.execute(sql)
            self.result = cursor.fetchall()
            return self.result
        except:
            print("Data Base Connection Failed to get subjec result data.....")
        conn.commit()
        cursor.close()
        conn.close()
        pass    # end of get_data_from_login_of_password

    def get_remarks(self):
        try:

            conn = sqlite3.connect(self.my_db)
            cursor = conn.cursor()
            sql = """SELECT remarks FROM subjec """
            cursor.execute(sql)
            self.remarks = cursor.fetchall()
            return self.remarks
        except:
            print("Data Base Connection Failed to get subjec remarks data.....")
        conn.commit()
        cursor.close()
        conn.close()
        pass    # end of fname get function





    pass  # end of data base class

if __name__ == "__main__":
    subjects_database = Subjec_Data_Base()
    #subjects_database.create_subjec_table()
    #subjects_database.insert_in_subjec_table(100,75,'Pass','V.Good')   
        #insert_in_subject_table ( total marks , marks obtained , result , remarks )
    subjects_id = subjects_database.get_subjectid_from_subjec()
    total_marks = subjects_database.get_total_marks()
    marks_obtained = subjects_database.get_marks_obtained()
    result = subjects_database.get_result()
    remarks = subjects_database.get_remarks()
    print(subjects_id)
    print(total_marks)
    print(marks_obtained)
    print(result)
    print(remarks)
    
    pass    # end of if name == main