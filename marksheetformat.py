
class Marksheetf:
    def __init__(self,rec):
        self.rec = rec

    def marksheetformat(self):
        for x in self.rec:
            print("\n")
            print("\t\t\t\t\t\t\tRGPV-BHOPAL")
            print("Roll no:",x[1] ,end="\t\t\t\t\t\t\t\t\t\t\t\t\t") 
            print("Course:",x[5])
            print("Name:",x[2],end="\t\t\t\t\t\t\t\t\t\t\t\t\t")
            print("Branch:",x[6])
            print("Father name:",x[3],end="\t\t\t\t\t\t\t\t\t\t\t\t")
            print("Sem:",x[7])
            print("Mother name:",x[4],end="\t\t\t\t\t\t\t\t\t\t\t\t")
            print("Year:",x[8])
            print("\n")
            # mark1 = x[9]
            # mark2 = x[10] 
            ls = [(101,"sub1",x[9]),(102,"sub2",x[10]),(103,"sub3",x[11]),(104,"sub4",x[12]),(105,"sub5",x[13])]
            # ls = [(101,"sub1")]
        
            print("\t    Sub code",end="\t")
            print("\tSub Name",end="\t")
            print("\tMax Mark",end="\t")
            print("\tMin Mark",end="\t")
            print("\tObtain Mark")

            for i in ls:
                print("\t    ",i[0],end="\t")
                print("\t",i[1],end="\t\t")
                print("\t 70",end="\t\t")
                print("\t 21",end="\t\t")
                print("\t",i[2])
                print("\n")
            
            sum = x[9]+x[10]+x[11]+x[12]+x[13]
            print("\t\t\t\t\t\t\t\t\t\t\t\t\tTotal: ",sum)
            print("\t\t\t\t\t\t\t\t\t\t\t\t\tPercentage:",(sum/5))
            if((sum/5)>=60):
                print("\t\t\t\t\t\t\t\t\t\t\t\t\tGrade: First class" ) 
            elif((sum/5)>=45):
                print("\t\t\t\t\t\t\t\t\t\t\t\t\tGrade: Second class")
            elif((sum/5)>=33):
                print("\t\t\t\t\t\t\t\t\t\t\t\t\tGrade: Third class")
            
            if x[9]<21 or x[10]<21 or x[11]<21 or x[12]<21 or x[12]<21:
                print("\t\t\t\t\t\t\t\t\t\t\t\t\tResult: Fail")
            else:
                print("\t\t\t\t\t\t\t\t\t\t\t\t\tResult: Pass")
            print("------------------------------------------------------------------------------------------------------------------------------------")
            print("\n")  

