f=open("abi.txt","w")
for i in range(5):
    roll=input("Please Enter Your Roll Number:")
    name=input("Please Enter Your Name:")
    marks=input("Please Enter Your Marks:")
    rec=(roll)+','+name+','+(marks)+','+'\n'
    f.write(rec)
    print(f)
f.close()
