
from marksheetformat import Marksheetf

def search():
    import mysql.connector as mysql
    mydb = mysql.connect(
        host= "localhost",
        user="root",
        password = "root",
        database = "newmarksheet"
    )
    
    def data():
        mycursor.execute(sql)
        rec = mycursor.fetchall()
        ob = Marksheetf(rec)
        ob.marksheetformat() 
    
    mycursor = mydb.cursor()
    

    while True:
        print("--------------------------------------------------------------------------------------------------------------")
        print("[1]search by Rollno\n[2]search by Name:\n[3]search by course\n[4]search by sem\n[5]Exit")
        print("--------------------------------------------------------------------------------------------------------------")
    
        n = int(input("Enter your choice: "))
        if n == 1:
            rollno = int(input("Enter a rollno: "))
            sql = "select * from marksheet where rollno = {0}".format(rollno)
            data()
        
        elif n==2:
            name = input("Enter your name: ")
            sql = "select * from marksheet where Name = '{0}'".format(name)
            data()

        elif n==3:
            course = input("Enter your course: ")
            sql = "select * from marksheet where course = '{0}'".format(course)
            data()

        elif n==4:
            sem = int(input("Enter your sem: "))
            sql = "select * from marksheet where sem = {0}".format(sem)
            data()
        
        elif n==5:
            break

if __name__ == "__main__":
    search()
