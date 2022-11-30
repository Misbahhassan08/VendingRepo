import sqlite3

class User_Data_Base:
    my_db = 'login.db'
    def __init__(self):
        print("My Login Data Base Is Working.....")
        pass    # end of __init__ function
    def create_login_table(self):
        try:

            conn = sqlite3.connect(self.my_db)
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS login
                        (userid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        username TEXT,
                        password TEXT,
                        fname TEXT,
                        lname TEXT,
                        subjectid INTEGER)""")
                           
            conn.commit()
            cursor.close()
            conn.close()
            print("Data Base login Table Created Successfully....")
        except:
            print("Data Base Connection Failed to create login table.....")
            pass    # end of create_login_table function
    
    def insert_in_login_table(self,username,password,fname,lname,subjectid):
        try:

            conn = sqlite3.connect(self.my_db)
            cursor = conn.cursor()
            cursor.execute(""" INSERT INTO login 
                               (username , password,fname,lname,subjectid)
                           VALUES 
                           (?,?,?,?,?)
                           """, (username,password,fname,lname,subjectid))
                           
            conn.commit()
            cursor.close()
            conn.close()
            print("Data Inserted Successfully in login Data base....")
        except:
            print("Login Data Base Connection Failed.....")
        pass    #end of insert function

    def get_user_data(self):
        try:

            conn = sqlite3.connect(self.my_db)
            cursor = conn.cursor()
            sql = """SELECT * FROM login """
            cursor.execute(sql)
            self.user = cursor.fetchall()
            conn.commit()
            cursor.close()
            conn.close()
            return self.user
        except:
            print("Data Base Connection Failed to get login lname data.....")
        
        pass    # end of fname get lname function



    pass  # end of data base class

if __name__ == "__main__":
    user_database = User_Data_Base()
    #user_database.create_login_table()
    #user_database.insert_in_login_table('admin6107','admin786','Amir','Mehmood',00)   
    #insert_in_login_table ( username , password , fname , lname , subjectid )
    userdata = user_database.get_user_data()
    print(userdata)
    
    pass