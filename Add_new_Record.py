
def newrecord():
    import mysql.connector as mysql
    mydb = mysql.connect(
        host= "localhost",
        user="root",
        password = "root",
        database = "newmarksheet"
    )
    
    n = int(input("How many record you want to add: "))
    for i in range(1,n+1):
        rollno = int(input("Enter your roll no: "))
        name = input("Enter your name: ") 
        fathername = input("Enter your father name: ")
        mothername = input("Enter your mother name: ")
        course = input("Enter your course name: ")
        branch = input("Enter your branch: ")
        sem = input("Enter your sem: ")
        year = input("Enter your year: ")
        sub1 = input("Enter mark of sub 1: ")
        sub2 = input("Enter mark sub 2: ")
        sub3 = input("Enter mark sub 3: ")
        sub4 = input("Enter mark sub 4: ")
        sub5 = input("Enter mark sub 5: ")
        mycursor = mydb.cursor()
        sql = "insert into marksheet(rollno,Name,Fathername,mothername,course,Branch,sem,year,sub1,sub2,sub3,sub4,sub5) values({0},'{1}','{2}','{3}','{4}','{5}','{6}','{7}',{8},{9},{10},{11},{12})".format(rollno,name,fathername,mothername,course,branch,sem,year,sub1,sub2,sub3,sub4,sub5)
        mycursor.execute(sql)
        mydb.commit()
        print("new record saved")
        mydb.close()
    
if __name__ == "__main__":
    newrecord()



