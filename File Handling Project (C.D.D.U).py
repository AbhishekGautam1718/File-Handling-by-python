import os
z=1
while(True):
    print("\n 1.Add Record:")
    print("\n 2.Display All Record:")
    print("\n 3.Search Student Record By Name:")
    print("\n 4.Search Student Record By Roll NO.:")
    print("\n 5.Delete Student Record By Name:")
    print("\n 6.Delete Student Record By Roll Number:")
    print("\n 7.Update Student Recodrd:")
    print("\n 8.Exit:")
    n=int(input("Please Enter Your Choice:"))
    if (n==8):
        break
    elif (n==1):
        print("Please Enter Student Record:")
        Name=input("Please Enter Your Name:")
        Roll=input("Please Enter Your Roll Number:")
        Pre=input("Please Enter Your Percentange:")
        Fees=input("Please Enter Your Fess(Per Month):")
        Class=input("Please Enter Your Class:")
        f=open("Abhishek.txt","a")
        f.write(Name+' - '+Roll+' - '+Pre+' - '+Fees+' - '+Class+"\n")
        f.close()
    elif (n==2):
        print("List Of Present Record")
        print("Name-RollNo.-Class-Fess-Precentage")
        f=open("Abhishek.txt","r")
        while(True):
            e=f.readline()
            l=len(e)
            if(l==0):
                break
            print(e.strip())
        f.close()
    elif(n==3):
        print("Search Record By Student Name")
        Search=input("Please Enter Student Name:")
        f=open("Abhishek.txt","r")
        flag=0
        while(True):
            t=f.readline()
            l=len(t)
            if (l==0):
                break
            g=t.split(' - ')
            if(g[0]==Search):
                print("Record Found")
                print("Name is:",g[0])
                print("Roll No.is:",g[1])
                print("Precentage is:",g[2])
                print("Fees is:",g[3])
                print("Class is:",g[4])
                flag=1
                break
        if (flag==0):
            print("Record Not Found")
        f.close()
    elif(n==4):
        print("Search Record By Student Roll Number")
        Search=input("Please Enter Student Roll Number:")
        f=open("Abhishek.txt","r")
        NF=0
        while(True):
            t=f.readline()
            l=len(t)
            if(l==0):
                break
            g=t.split(" - ")
            if(g[1]==Search):
                print("Record Found")
                print("Name is:",g[0])
                print("Roll No.is:",g[1])
                print("Precentage is:",g[2])
                print("Fees is:",g[3])
                print("Class is:",g[4])
                flag=1
                break
        if(NF==0):
            print("Record Not Found")
        f.close()
    elif(n==5):
        print("Delete Student Record By Name")
        Delete=input("Please Enter Your Name:")
        f=open("Abhishek.txt","r")
        o=open("Tem.txt","w")
        NF=0
        A=0
        while(True):
            t=f.readline()
            l=len(t)
            if(l==0):
                break
            g=t.split(" - ")
            if(g[0]!=Delete):
                o.write(t)
            if(g[0]==Delete):
                A=1
        f.close()
        o.close()
        if(A==1):
            print("Record Delete Succesfully")
            os.remove("Abhishek.txt")
            os.rename("Tem.txt","Abhishek.txt")
        elif(A==0):
            print("Record Is Not Delete:")
    elif(n==6):
        print("Delete Student Record By Roll Num.:")
        Delete=input("Please Enter Your ROll Num.:")
        f=open("Abhishek.txt","r")
        o=open("Tem.txt","w")
        NF=0
        A=0
        while(True):
            t=f.readline()
            l=len(t)
            if(l==0):
                break
            g=t.split(" - ")
            if(g[1]!=Delete):
                o.write(t)
            if(g[1]==Delete):
                A=1
        f.close()
        o.close()
        if(A==1):
            print("Record Delete Succesfully")
            os.remove("Abhishek.txt")
            os.rename("Tem.txt","Abhishek.txt")
        elif(A==0):
            print("Record Is Not Delete:")
        
    elif(n==7):
        print("Update Student Record By Name:")
        Update=input("Please Enter Your Name:")
        f=open("Abhishek.txt","r")
        o=open("Tem.txt","w")
        NF=0
        while(True):
            t=f.readline()
            l=len(t)
            if(l==0):
                break
            g=t.split(" - ")
            if(g[0]==Update):
                print("Current Detail Is=",t)
                print("*"*20)
                UR=input("If You Want To Update Your Roll Number Then Enter Your 'New Roll Number' Othrwise Press 'Enter' To Continue:")
                UP=input("If You Want To Update Your Percentage Then Enter Your 'New Percentage' Othrwise Press 'Enter' To Continue:")
                UF=input("If You Want To Update Your Fees Then Enter Your 'New Fess' Othrwise Press 'Enter' To Continue:")
                UC=input("If You Want To Update Your Class Then Enter Your 'New Class' Othrwise Press 'Enter' To Continue:")
                
                
                if len(UR)==0:
                    UR=g[1]
                if len(UP)==0:
                    UP=g[2]
                if len(UF)==0:
                    UF=g[3]
                if len(UC)==0:
                    UC=g[4]
                o.write(g[0]+' - '+UR+' - '+UP+' - '+UF+' - '+UC)
                A=1
            else:
                o.write(t)
        f.close()
        o.close()
        if(A==1):
            print("Record Updated Succesfully")
            os.remove("Abhishek.txt")
            os.rename("Tem.txt","Abhishek.txt")
        elif(A==0):
            print("Record Is Not Updated:")
