import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5 import QtWidgets


class Database:
    dataBase_name = 'Data.db'

    def __init__(self):
        print('its work')
        pass

    def insertuser(self, username, userpassword, withdraw_limit, role):
        try:

            conn = sqlite3.connect(self.dataBase_name)
            cursor = conn.cursor()

            cursor.execute("""
                               CREATE TABLE IF NOT EXISTS user
                               (UID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                               username TEXT, 
                               password TEXT,
                               withdrawlimit TEXT,
                               role )""")

            cursor.execute(""" INSERT INTO user 
                               (username , password, withdrawlimit, role)
                           VALUES 
                           (?,?,?,?)
                           """, (username, userpassword, withdraw_limit, role))

            conn.commit()
            cursor.close()
            conn.close()
            return True
        except:
            print('Error in Data base: Inserting Temp Values')
            return False

    def del_user(self, _id):
        id = int(_id)
        print('deleting data base please wait')
        if id < 1:
            return False
        conn = sqlite3.connect(self.dataBase_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM user WHERE UID = ?", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    def edit_user(self, _id, _username, _pin, _withdraw, _role):
        id = int(_id)
        un = _username
        pin = _pin
        wd = _withdraw
        rol = _role
        print('Updating User now please wait ....')
        conn = sqlite3.connect(self.dataBase_name)
        if id < 0:
            return False
        cursor = conn.cursor()
        cursor.execute("UPDATE user set username = ? ,password = ?,withdrawlimit = ?,role = ? WHERE UID = ?",
                       (un, pin, wd, rol, id))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    def check_id(self, _id):
        id = int(_id)
        print('checking ID now from edit frame')
        conn = sqlite3.connect(self.dataBase_name)
        if id < 0:
            return False
        else:
            print('checking Edit id details please wait ')

            cursor = conn.cursor()
            cursor.execute("SELECT username,password,withdrawlimit,role FROM user WHERE UID = {}".format(id))
            val = cursor.fetchall()
            if len(val) >= 1:

                for x in val:
                    # print('1 - {} , 2- {} , 3- {}, 4- {} '.format(x[0], x[1], x[2], x[3]))
                    return x
            else:
                return 'Null'

    def check_login(self, _userName, _userPassword):
        conn = sqlite3.connect(self.dataBase_name)
        if len(_userName) <= 1 and len(_userPassword) <= 1:
            return False
        else:
            print('checking login details please wait ')
            username = _userName
            password = _userPassword
            cursor = conn.cursor()
            cursor.execute("SELECT UID, username, password, role FROM user where username = ? and password = ?",
                           (username, password))
            val = cursor.fetchall()
            if len(val) > 0:
                for x in val:
                    print(x)
                    return x
            else:
                return False

    def show_users_data(self):
        try:
            print('In show user database calling')
            db = sqlite3.connect(self.dataBase_name)
            sql = 'SELECT * from user'
            cur = db.cursor()
            cur.execute(sql)
            db.close()
            while True:
                record = cur.fetchone()
                if record is None:
                    break
            db.close()
        except:
            print('Error in fetching Users')

    def fetch_new_user_id(self):
        try:
            print('In fetch_new_user_idcalling')
            db = sqlite3.connect(self.dataBase_name)
            sql = 'SELECT * from user'
            cur = db.cursor()
            cur.execute(sql)
            record = cur.fetchall()
            for x in record:
                self.j = x
            db.close()
            return self.j
        except:
            print('Error in fetching Users')
            return False

    # -----------------------------------------------------------------------------------------------------------------------
    def insert_transaction(self, uid, deposit, withdraw, datetime, money_left, purpose):
        conn = sqlite3.connect(self.dataBase_name)
        cursor = conn.cursor()
        cursor.execute("""
                                       CREATE TABLE IF NOT EXISTS trans 
                                       (TID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                       UID INTEGER,
                                       deposit TEXT, 
                                       withdraw TEXT,
                                       datetime TEXT,
                                       money_left TEXT,
                                       purpose TEXT
                                       )""")

        print('Data base transaction created')
        cursor.execute(""" INSERT INTO trans (UID, deposit, withdraw, datetime,money_left, purpose)
                                   VALUES 
                                   (?,?,?,?,?,?)
                                   """, (uid, deposit, withdraw, datetime, money_left, purpose))

        conn.commit()
        print('done')
        cursor.close()
        conn.close()
        return True

    def show_transaction_data(self, id):
        print('In show transaction database calling')
        db = sqlite3.connect(self.dataBase_name)
        sql = 'SELECT * from trans where UID = {}'.format(id)
        cur = db.cursor()
        cur.execute(sql)
        v = cur.fetchall()
        print(v)
        db.close()
        for x in v:
            j = x

            return j

    def delete_transaction(self, id):

        print('deleting transaction data please wait')
        conn = sqlite3.connect(self.dataBase_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM trans WHERE UID = ?", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    def fetch_last_transaction(self, id):
        global j
        print('In show transaction last row in database calling')
        db = sqlite3.connect(self.dataBase_name)
        sql = 'SELECT * from trans where UID = {}'.format(id)
        cur = db.cursor()
        cur.execute(sql)

        v = cur.fetchall()
        db.close()
        for x in v:
            j = x
        return j


    # ----------------------------------------------------------------------------------------------------------------------------
    def insert_note(self, uid, tid, money):
        conn = sqlite3.connect(self.dataBase_name)
        cursor = conn.cursor()
        cursor.execute("""
                                               CREATE TABLE IF NOT EXISTS note 
                                               (NID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                               UID INTEGER,
                                               TID INTEGER, 
                                               money_left TEXT
                                               )""")

        print('Data base transaction created')
        cursor.execute(""" INSERT INTO trans (UID, TID, money_left)
                                           VALUES 
                                           (?,?,?)
                                           """, (uid, tid, money))
        conn.commit()
        print('done')
        cursor.close()
        conn.close()
        return True

    def update_note(self, uid, tid, money):
        print('Updating Note now please wait ....')
        conn = sqlite3.connect(self.dataBase_name)
        cursor = conn.cursor()
        cursor.execute("UPDATE note set UID = ? , TID = ?, money_left = ?",
                       (uid, tid, money))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    # -----------------------------------------------------------------------------------------------------------------------

    def delete_log(self):
        print('deleting data base please wait')
        conn = sqlite3.connect(self.dataBase_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM log1 WHERE log = 1")
        conn.commit()
        cursor.close()
        conn.close()
        return True

    def search_login_person(self):
        conn = sqlite3.connect(self.dataBase_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * from log1 where log = 1")
        val = cursor.fetchall()
        return val

    def update_login_person(self, lid, uid, datetime):
        print('Updating login person now please wait ....')
        conn = sqlite3.connect(self.dataBase_name)
        cursor = conn.cursor()
        cursor.execute("UPDATE log1 set UID = ? , log = 0, datetime = ? WHERE LID = ?",
                       (uid, datetime, lid))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    def update_login_person_purpose(self, lid, purpose):
        print('Updating login person purpose now please wait ....')
        conn = sqlite3.connect(self.dataBase_name)
        cursor = conn.cursor()
        cursor.execute("UPDATE log1 set  password = ? WHERE LID = ?",
                       (purpose, lid))
        conn.commit()
        cursor.close()
        conn.close()
        return True
        pass

    def insert_login_person(self, uid, log, username, userpassword, role, datetime):
        conn = sqlite3.connect(self.dataBase_name)
        cursor = conn.cursor()

        cursor.execute("""
                                       CREATE TABLE IF NOT EXISTS log1
                                       (LID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                       UID INTEGER,
                                       log INTEGER,
                                       username TEXT, 
                                       password TEXT,
                                       role TEXT,
                                       datetime TEXT
                                       )""")

        cursor.execute(""" INSERT INTO log1
                                       (UID,log,username,password,role,datetime)
                                   VALUES 
                                   (?,?,?,?,?,?)
                                   """, (uid, log, username, userpassword, role, datetime))

        conn.commit()
        cursor.close()
        conn.close()
        return True

    # -------------------------------------------------------------------------------------------------------------------

    def insert_denomination(self, d1, d2, d3, currency):
        try:

            conn = sqlite3.connect(self.dataBase_name)
            cursor = conn.cursor()

            cursor.execute("""
                               CREATE TABLE IF NOT EXISTS denomination
                               (DID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                               d1 TEXT, 
                               d2 TEXT,
                               d3 TEXT,
                               currency TEXT
                               )""")

            cursor.execute(""" INSERT INTO denomination 
                               (d1,d2,d3,currency)
                           VALUES 
                           (?,?,?,?)
                           """, (d1, d2, d3, currency))

            conn.commit()
            cursor.close()
            conn.close()
            return True
        except:
            print('Error in Data base: Inserting transactions Values')
            return False

    def update_denomination(self, d1, d2, d3, currency):
        print('Updating transaction method now please wait ....')
        conn = sqlite3.connect(self.dataBase_name)
        cursor = conn.cursor()
        cursor.execute("UPDATE denomination set d1 = ? ,d2 = ?,d3 = ?,currency = ? WHERE DID = 1",
                       (d1, d2, d3, currency))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    def get_den(self):
        conn = sqlite3.connect(self.dataBase_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * from denomination")
        val = cursor.fetchall()
        conn.close()
        return val

    def test_db(self):
        conn = sqlite3.connect(self.dataBase_name)
        cursor = conn.cursor()
        cursor.execute("SELECT trans.TID, user.username , trans.deposit, trans.withdraw , trans.datetime, trans.money_left, trans.purpose  from trans left join user where user.UID = trans.UID")
        val = cursor.fetchall()
        conn.close()
        return val



