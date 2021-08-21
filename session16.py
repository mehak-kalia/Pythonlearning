#persistance cloud
"""create database
create the tables using SQL
ORM object relational mapping
map objects attributes as tables columns

sql command
create Table User(
    uid int primary key auto_increment,
    name varchar(256),
    phone varchar(256),
    email varchar(256) )
     to add a row in a table
     insert into User1 values(null, 'john' , '112837723027' , '@sth')
      to update a row in table
    update User set name='Leo Watson', phone='+91 98761 12345', email='leo.watson@example.com' where uid = 3
    update User set name='Leo Watson', email='leo.watson@example.com' where uid = 3 // skip phone number
    to delete row from table
    delete from User where uid = 1
    to see all the rows
    select * from User                  // all columns
    select name, phone from User        // selective columns
    select * from User where uid = 1    // filter | >, <, =, and

    Steps to Communicate with DataBase
    1. Download the library and install it in your python project
        > Either: Settings > Project Interpreter > + to install > mysql-connector
        > OR    : pip install mysql-connector on Terminal
    2. Write SQL Statement
    3. import library in our project
    4. Create Connection with DataBase
    5. From the Connection Obtain Cursor, which performs all the DB Operations i.e. Execution of SQL Statements
    6. Execute the SQL Statement with cursor and commit :) """

import mysql.connector as db

class User1:
    def __init__(self):
        self.name = input("enter your name")
        self.phone = input("enter your phone no.")
        self.email = input("enter your email")
    def show(self):
        print("your details are :\n {} | {} | {}".format(self.name, self.phone, self.email))
    def RegisterUser(self):
        sql = "insert into User1 values(null, '{}' , '{}' , '{}')".format(self.name, self.phone, self.email)

        connection = db.connect(user="root", password = "", database = "mehak", host = "localhost", port = "3306")
        print("connection created")
        cursor = connection.cursor()

        cursor.execute(sql)
        connection.commit()

        print("user data saved")

    def UpdateUser(self):
        self.uid = input("enter user's uid")
        self.name = input("enter your name")
        self.phone = input("enter your phone no.")
        self.email = input("enter your email")


        sql = "update User1 set name = '{}', phone = '{}',email = '{}' where uid = '{}'".format(self.name, self.phone, self.email, self.uid)

        connection = db.connect(user="root", password="", database="mehak", host="localhost", port="3306")
        print("connection created")
        cursor = connection.cursor()

        cursor.execute(sql)
        connection.commit()

        print("user data updated")

    def DeleteUser(self):
        sql = "delete from User where uid = {}".format(self.uid)

        connection = db.connect(user="root", password="", database="mehak", host="localhost", port="3306")
        print("connection created")
        cursor = connection.cursor()

        cursor.execute(sql)
        connection.commit()

        print("user data deleted")

    def fetch_all_user(self):
        sql = "select * from User1"

        connection = db.connect(user="root", password="", database="mehak", host="localhost", port="3306")
        print("connection created")
        cursor = connection.cursor()

        cursor.execute(sql)
        rows = cursor.fetchall()#list of all the rows that are in the form of tuples
        for row in rows:
            #print(row)
             print(row[0], row[1], row[2], row[3])

        print("user data found")

    def fetchuser(self, uid):

        sql = "select * from User1 where uid = {}".format(uid)

        connection = db.connect(user="root", password="", database="mehak", host="localhost", port="3306")
        print("connection created")
        cursor = connection.cursor()

        cursor.execute(sql)
        rows = cursor.fetchall()#list of all the rows that are in the form of tuples
        for row in rows:
            #print(row)
             print(row[0], row[1], row[2], row[3])

def main():
    uref = User1()
    #uref.show()
    """choice = input("would you like to save the user yes/no")
    if choice == "yes":
        uref.RegisterUser()
        
        print("thanks for using the software")"""
    #uref.fetch_all_user()
    uref.fetchuser(uid=input("enter uid"))
    print("thanks for using the software")
if __name__ == '__main__':
    main()