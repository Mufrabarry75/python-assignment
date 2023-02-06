
def studentlist():
    StudList=[]
    choice= 'y'
    while (choice == 'y'):
       studname= input("enter student name")
       StudList.append(studname)
       choice= input("enter your choice [y/n]")

studentlist()
