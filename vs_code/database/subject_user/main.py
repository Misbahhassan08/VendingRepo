from Admin_Detail import Ui_Dialog
from add_detail import Ui_AddDetail
from login import Ui_Login
from User_Detail import Ui_Detail
from logintable import User_Data_Base
from subject_table import Subjec_Data_Base
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from functions import Functions

class loginscreen(QtWidgets.QWidget,Ui_Login):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
    pass    #end of loginscreen class



class user_detail_screen(QtWidgets.QWidget,Ui_Detail):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
    pass    # end of detailscreen class

class admin_detail_screen(QtWidgets.QWidget,Ui_Dialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
    pass    # end of detailscreen class

class Add_Detail_Screen(QtWidgets.QTabWidget,Ui_AddDetail):
    def __init__(self):
        QtWidgets.QTabWidget.__init__(self)
        self.setupUi(self)
    pass    #  end of Add_Detail_screen



class _main:
    def __init__(self):
        self.login_screen = loginscreen()
        self.user_detail_screen = user_detail_screen()
        self.user_database = User_Data_Base()
        self.subjec_database = Subjec_Data_Base()
        self.admin_screen = admin_detail_screen()
        self.add_detail_screen = Add_Detail_Screen()
        self.functions = Functions()
        self.login_screen.show()
        self.admin_screen.addbutton.clicked.connect(self.insert_event)
        self.admin_screen.deletebutton.clicked.connect(self.Delete_event)
        self.login_screen.pushButton.clicked.connect(self.login_event)
        self.admin_screen.updatebutton.clicked.connect(self.Update_event)
        
        pass    # end of __init__

    def login_event(self):
        self.username_from_text = self.login_screen.lineEdit.text()
        self.password_from_text = self.login_screen.lineEdit_2.text()
        self.user_detail_data_ =  self.functions.put_username_password_get_user_detail(self.username_from_text,self.password_from_text)
        self.student_fname_ = self.functions.put_username_password_students_fname(self.username_from_text,self.password_from_text)
        self.admin_fname_ = self.functions.put_username_password_admin_fname(self.username_from_text,self.password_from_text)
        self.student_detail_data_ = self.functions.put_username_password_get_admin_data(self.username_from_text,self.password_from_text)
        print(self.student_fname_)
        print(self.admin_fname_)
        if self.student_fname_ != None :
            self.user_detail_screen.show()
            for f_row , f_column_data in enumerate(self.student_fname_):
                for f1_row , f1_column_data in enumerate(f_column_data):
                    self.user_detail_screen.label.setText(f"Welcome Dear {f1_column_data}")
            for sd_row , sd_column_data in enumerate(self.user_detail_data_):
                sd_row + 1
                for sd_column_row , sd_column_data1 in enumerate(sd_column_data):
                    self.user_detail_screen.tableWidget.setItem(sd_row, sd_column_row, QtWidgets.QTableWidgetItem(str(sd_column_data1)))
                break
        elif self.admin_fname_ != None:
             self.admin_screen.show()
             for f_row1 , f_column_data1 in enumerate(self.admin_fname_):
                 for f1_row1 , f1_column_data1 in enumerate(f_column_data1):
                    self.admin_screen.label.setText(f"Welcome Dear {f1_column_data1}") 
             for sd_row2 , sd_column_data2 in enumerate(self.student_detail_data_):
                 self.admin_screen.tableWidget.insertRow(sd_row2)
                 for sd_column_row2 , sd_column_data3 in enumerate(sd_column_data2):
                    self.admin_screen.tableWidget.setItem(sd_row2, sd_column_row2, QtWidgets.QTableWidgetItem(str(sd_column_data3)))

        pass   

    def insert_event(self):
        self.add_detail_screen.show()
        self.add_detail_screen.pushButton.clicked.connect(self.insert_event_performe)
        pass    # end of insert_event
    def insert_event_performe(self):
        try:
            self.insert_username = self.add_detail_screen.textEdit.toPlainText()
            self.insert_password = self.add_detail_screen.textEdit_2.toPlainText()
            self.insert_fname = self.add_detail_screen.textEdit_3.toPlainText()
            self.insert_lname = self.add_detail_screen.textEdit_4.toPlainText()
            self.insert_subjectid = self.add_detail_screen.textEdit_5.toPlainText()
            self.insert_result = self.add_detail_screen.textEdit_6.toPlainText()
            self.insert_remarks = self.add_detail_screen.textEdit_7.toPlainText()
            self.insert_marks_obtained = self.add_detail_screen.textEdit_8.toPlainText()
            self.insert_total_marks = self.add_detail_screen.textEdit_9.toPlainText()
            self.user_database.insert_in_login_table(self.insert_username,self.insert_password,self.insert_fname,self.insert_lname,int(self.insert_subjectid))   
                                #insert in login table ( username , password , fname , lname , subjectid )
            self.subjec_database.insert_in_subjec_table(int(self.insert_total_marks),int(self.insert_marks_obtained),self.insert_result,self.insert_remarks)   
                                #insert in subject table ( total marks , marks obtained , result , remarks )
            self.add_detail_screen.label_7.setText(f"Status : Added Successfully.......")
            self.admin_screen.statuslabel.setText("Status : Data Added Successfully......")
            self.add_detail_screen.textEdit.setText("")
            self.add_detail_screen.textEdit_2.setText("")
            self.add_detail_screen.textEdit_3.setText("")
            self.add_detail_screen.textEdit_4.setText("")
            self.add_detail_screen.textEdit_5.setText("")
            self.add_detail_screen.textEdit_6.setText("")
            self.add_detail_screen.textEdit_7.setText("")
            self.add_detail_screen.textEdit_8.setText("")
            self.add_detail_screen.textEdit_9.setText("")
        except:
            self.add_detail_screen.label_7.setText("Status : Value Type Error!!!!")
        pass    # end of insert event performe
    def Delete_event(self):
        row = self.admin_screen.tableWidget.currentRow()
        check  = self.admin_screen.tableWidget.item(row,5)
        subject_id_value = check.text()
        self.functions.put_subjectid_delete_data(subject_id_value)
        self.admin_screen.statuslabel.setText("Status : Selected Row Deleted Successfully")
        pass    # end of delete event

    def Update_event(self):
        row = self.admin_screen.tableWidget.currentRow()
        user = self.admin_screen.tableWidget.item(row,0)
        username = self.admin_screen.tableWidget.item(row,1)
        password = self.admin_screen.tableWidget.item(row,2)
        fname = self.admin_screen.tableWidget.item(row,3)
        lname = self.admin_screen.tableWidget.item(row,4)
        user_id = user.text()
        username1 = username.text()
        password1 = password.text()
        fname1 = fname.text()
        lname1 = lname.text()
        self.functions.selected_data_update(username1,password1,fname1,lname1,int(user_id))
        self.admin_screen.statuslabel.setText("Status : Data Updated Successfully....")
               # selected data update (username,passsword,firstname,lastname,where userid)
        
            #self.functions.put_subjectid_delete_data(subject_id_value)
            #self.admin_screen.statuslabel.setText("Status : Selected Row Deleted Successfully")
        pass    # end of update event

    pass    # end of _main   class


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = _main()
    sys.exit(app.exec_())
    pass    # end of main function



if __name__ == "__main__":
    import sys
    main()
    pass    # end of main