
from marksheetformat import Marksheetf

def marksheet():
    import mysql.connector as mysql

    mydb = mysql.connect(
    host= "localhost",
    user="root",
    password = "root",
    database = "newmarksheet"
    )

    mycursor = mydb.cursor()
    # rollno = int(input("Enter a rollno: "))
    # sql = "select * from marksheet where rollno = {0}".format(rollno)
    sql = "select * from marksheet"
    mycursor.execute(sql)
    rec = mycursor.fetchall()
    print(rec)
    ob = Marksheetf(rec)
    ob.marksheetformat()
         
if __name__ == "__main__":
    marksheet()
