from Add_new_Record import newrecord
from deletemarksheet import delete
from update import update
from marksheetshow import marksheet
from search  import search
from count import count

while True:
    print("--------------------------------------------------------------------------------------------------------------")
    print("[1]Add new record\n[2]Delete a record\n[3]Update\n[4]All marksheet\n[5]search\n[6]Exit\n")
    print("--------------------------------------------------------------------------------------------------------------")
    n = int(input("Enter your choice: "))
    if n==1:
        newrecord()
    
    elif n==2:
        delete()

    elif n==3:
        update()


    elif n==4:
        count()
        marksheet()
    
    elif n==5:
        search()
    
    elif n==6:
        break

