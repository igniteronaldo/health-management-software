from typing import TextIO

name = {1: "Harry", 2: "Rohan", 3: "ann"}
work = {1: "Exercise", 2: "Diet"}


def getdate():
    import datetime
    return datetime.datetime.now()


try:
    print("hello welcome to health managemnet sysytem")
    for key,naam in name.items():
        print("press",key,"for",naam,"\n",end="")
    aapkanaam=int(input("please let us know who are you by typing your number from the above list:"))
    print("\nwelcome",name[aapkanaam],"to our very natural and beautiful health management system")

    decision="please let me know whether u have come here for exercise purpose or diet purpose"
    print(decision)

    for echa,kyun in work:
        print("press",echa,"for",kyun,"\n",end="")
    kya=int(input("Toh kya socha aapne"))
    if kya==1:
       f=open(name[aapkanaam]+"exercise"+"txt","r+")
    elif kya== 2:
       f = open(name[aapkanaam]+"diet"+"txt","r+")
    else:
        print(name[aapkanaam],"please check your input again")

    print("1.if u want to retreieve then please press 1"
          "2.if u want to log then please press 2")
    character=int(input("wheher u want to log or retrieve,please let us know to give u better:"))
    if character==1:
        print("you can write whatever u want to write now since u have selected to log:")
        mytext=input()
        f.write("["+ str(getdate())+"]:"+mytext+"\n")
        f.close()
    elif character==2:
        print("sorry! you cannot add anything now but once your file gets created then u can make changes")
        f = open(name[aapkanaam], work[kya] + "txt")
    else:
        print(name[aapkanaam],"please put proper number")
except:
       print("sorry!your file cannot be created\n"
             "it seems like you have made a mistake while processing the above forum\n"
             "please fill it up properly the next time")
print("THANK YOU FOR USING OUR HEALTH MANAGEMENT SYSTEM\n"
      "A PRODUCT BY\n -"
      "TIWARI AND CO\n")






