from ast import And
from fnmatch import fnmatchcase
from pstats import Stats
import sqlite3


class Functions:
    my_db = 'login.db'
    def put_username_password_get_user_detail(self,enteredusername,enteredpassword):
        try:
            conn = sqlite3.connect(self.my_db)
            cursor = conn.cursor()
            cursor.execute("""SELECT subjec.subjectid,login.userid,total_marks,marks_obtained,result,remarks 
                        FROM subjec,login 
                        WHERE  username = ? AND password = ? """,
                        (enteredusername,enteredpassword))
            self.table_data = cursor.fetchall()
            conn.commit()
            cursor.close()
            conn.close()
            return self.table_data
        except:
           print("Data Base Connection Failed to get table data.....")
            
        pass  # end of put username , password  function

    def put_username_password_get_admin_data(self,enteredusername2,enteredpassword2):
        try:
            if enteredusername2 == 'admin6107' :
                if enteredpassword2 == 'admin786' :
                    conn = sqlite3.connect(self.my_db)
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM login")
                    self.student_data = cursor.fetchall()
                    
                    conn.commit()
                    cursor.close()
                    conn.close()
                    return self.student_data
                

        except:
           print("Data Base Connection Failed to get stdudents data.....")
            
        pass  # end of put username , password  function

    def put_username_password_students_fname(self,enteredusername1,enteredpassword1):
        try:
            if enteredusername1 != 'admin6107' and enteredpassword1 != 'admin786':
                conn = sqlite3.connect(self.my_db)
                cursor = conn.cursor()
                cursor.execute("""SELECT fname 
                        FROM login
                        WHERE username = ? AND password = ? """,    #login.subjectid = subjec.subjectid 
                        (enteredusername1,enteredpassword1))
                self.fname_data1 = cursor.fetchall()
                conn.commit()
                cursor.close()
                conn.close()
                return self.fname_data1
        except:
           print("Data Base Connection Failed to get fname data.....")
            
        pass  # end of put username , password  function

    def put_username_password_admin_fname(self,enteredusername3,enteredpassword3):
        try:
            if enteredusername3 == 'admin6107' :
                if enteredpassword3 == 'admin786' :
                    conn = sqlite3.connect(self.my_db)
                    cursor = conn.cursor()
                    cursor.execute("""SELECT fname 
                        FROM login
                        WHERE username = 'admin6107'""")
                    self.fname_admin = cursor.fetchall()
                    
                    conn.commit()
                    cursor.close()
                    conn.close()
                    return self.fname_admin
        except:
           print("Data Base Connection Failed to get fname data.....")

    def put_subjectid_delete_data(self,enteredid):
        try:
            conn = sqlite3.connect(self.my_db)
            cursor = conn.cursor()
            cursor.execute("""Delete FROM login where subjectid = ?""" , str(enteredid,))
            cursor.execute("""Delete FROM subjec where subjectid = ?""" , str(enteredid,))
            self.datee = cursor.fetchall()
            conn.commit()
            cursor.close()
            conn.close()
            status = "Selected ID Deleted Successfully...."
            return self.datee
        except:
            print("Data Base Connection Failed to delete entered ID data.....")
            
            pass  # end of put username , password  function

    def selected_data_update(self,username,password,fname,lname,userid):
        #try:
            conn = sqlite3.connect(self.my_db)
            cursor = conn.cursor()
            cursor.execute("""UPDATE login SET username = ? , password = ? , fname = ? ,
             lname = ? WHERE userid = ? """, (username,password,fname,lname,userid))
            conn.commit()
            cursor.close()
            conn.close()
            status = "Selected row updated Successfully...."
            print(status)
        #except:
            #print("Data Base Connection Failed to update entered ID data.....")
            
            pass  # end of selected data update , password  function
    pass

if __name__ == "__main__":
    function =  Functions()
    #feedback =  function.put_subjectid_delete_data(4)
    #print(feedback)
    #function.selected_data_update('ali6107','ali786','Ali','Murtza',13)
                # selected data update (username,passsword,firstname,lastname,where userid)
    pass