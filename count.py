
def count():
    import mysql.connector as mysql
    mydb = mysql.connect(
        host= "localhost",
        user="root",
        password = "root",
        database = "newmarksheet"
    )

    mycursor = mydb.cursor()
    sql = "select count(*) from marksheet"
    mycursor.execute(sql)

    for x in mycursor:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tNumber of marksheets:",x[0])

if __name__ == "__main__":
    count()






