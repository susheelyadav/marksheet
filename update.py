
def update():
    import mysql.connector as mysql
    mydb = mysql.connect(
        host= "localhost",
        user="root",
        password = "root",
        database = "newmarksheet"
    )
    while True:
        print("--------------------------------------------------------------------------------------------------------------")
        print("[1]Update a marks\n[2]Update a Branch\n[3]Update a Year\n[4]Exit\n")
        print("--------------------------------------------------------------------------------------------------------------")
        n = int(input("Enter your choice: "))
        mycursor = mydb.cursor()
        if n == 1:
            rollno = int(input("Enter a roll no: "))
            n = int(input("Enter the number of subject: "))
            i = 1
            while i<=n:
                sub = input("Enter a subject name: ")
                marks = input("Enter your updated marks: ")    
                sql = "UPDATE marksheet  SET {0} = {1} WHERE rollno = {2}".format(sub,marks,rollno)
                mycursor.execute(sql)
                mydb.commit()
                i+=1
            print("Marksheet updated....")
        
        elif n == 2:
            rollno = int(input("Enter a roll no: ")) 
            branch = input("Enter updated branch name: ")
            sql = "UPDATE marksheet  SET Branch = '{0}' WHERE rollno = {1}".format(branch,rollno)
            mycursor.execute(sql)
            mydb.commit()
            print("Marksheet updated....")
        
        elif n == 3:
            rollno = int(input("Enter a roll no: "))
            sem = int(input("Enter updated sem : "))
            year = int(input("Enter updated year : "))
            sql = "UPDATE marksheet  SET sem = {0},year={1} WHERE rollno = {2}".format(sem,year,rollno)
            mycursor.execute(sql)
            mydb.commit()
            print("Marksheet updated....")
        
        elif n == 4:
            break


if __name__ == "__main__":
    update()