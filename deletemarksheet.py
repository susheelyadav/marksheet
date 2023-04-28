
def delete():
    rollno = int(input("Enter a roll number: "))
    import mysql.connector as mysql
    mydb = mysql.connect(
        host= "localhost",
        user="root",
        password = "root",
        database = "newmarksheet"
    )
    mycursor = mydb.cursor()
    sql = "delete from marksheet where rollno={0}".format(rollno)
    mycursor.execute(sql)
    mydb.commit()
    mydb.close()
    print("you marksheet is deleted")

if __name__ == "__main__":
    delete()

