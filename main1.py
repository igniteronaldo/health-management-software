import colorama
from colorama import Fore,Style,Back
colorama.init()
print(Style.BRIGHT)
print(Fore.BLACK)
print(Style.BRIGHT)
print("                        ""WE ARE HERE JUST FOR YOU\n"
      "                                             ""YOU ARE OUR FIRST PRIORITY\n")
print(Style.RESET_ALL)
echu=input("Write 'health' key on keyboard to continue:")
for an in echu:
    if echu=='health':
        print("                                                      ",  Style.BRIGHT,Fore.RED,"|| HEALTH",Style.BRIGHT,
              Fore.BLACK,
              "MANAGEMENT",
                                                                                  Style.BRIGHT,Fore.RED,"SYSTEM  ||")
    else:
        print("                                                      ", Style.BRIGHT, Fore.RED, "|| HEALTH",Style.BRIGHT,
              Fore.BLACK,
              "MANAGEMENT",
                                                                                  Style.BRIGHT, Fore.RED, "SYSTEM  ||")
    break
print(Style.RESET_ALL)
print(Style.DIM)
print(Fore.LIGHTYELLOW_EX)
print("\n\nBELOW IS OUR TERMS AND CONDITIONS FOR YOUR HEALTH AND ALSO ABOUT US:\n")
print("please wait for some time\n\n")
print(Style.RESET_ALL)
import wikipedia
print(Fore.GREEN)
print(wikipedia.summary("Healthcare in India"))


print(Style.RESET_ALL)
print(Style.DIM)
print(Fore.LIGHTYELLOW_EX)
print("\n\nIF YOU ARE A NEW MEMBER IN OUR SYSTEM THEN PLEASE WRITE YOUR NAME BELOW.\n")
pocho=input("Please tell us whether you are a member of our system.\n"
            "Press small 'y' for YES and\n"
            "Press small 'n' for NO.")
Gamu = "EMPTY(NO REGISTERED MEMBER FOR THIS NUMBER.)😎"
for naming in pocho:
    try:
       if pocho=='n':
          Gamu=input("PLEASE TYPE YOUR NAME HERE:")
          print("THANKS FOR JOINIIG OUR HEALTH SYSTEM",Gamu)
       else:
          print("IT MEANS YOU ARE ALREADY IN THE GROUP")
    except Exception as e:
          print()
name = {1: "Harry", 2: "Rohan", 3: "Aniket", 4: "kamakhya", 5: "Asha", 6: "Nilesh", 7: " Madhu",8: "Mansi ",9: Gamu}
work = {1: "Exercise", 2: "Diet"}

def getdate():
    import datetime
    return datetime.datetime.now()
try:
    print("HELLO,\nYOU ARE WELCOMED TO HEALTH MANAGEMENT SYSTEM.")
    for key, naam in name.items():
        print("Press", key, "For", naam,"\n", end="")
    aapkanaam = int(input("Please let us know who are you by typing your number from the above list:"))
    print("\nWelcome",name[aapkanaam],"to our very natural and beautiful Health Management System.")

    def text():
        """DO U WANT TO LOG OR RETRIEVE?
           LOG WILL HELP YOU ADD TO YOUR EXERCISE OR DIET DURING THE CREATION OF YOUR FILE.
           WHEREAS RETRIEVE WILL NOT ALLOW YOU TO ADD DETAILS TO YOUR FILE ONLY AFTER COMPLISION. """
    print(text.__doc__)
    batao = ("\nPress 1 to Log and\n" 
             "Press 2  to Retrieve\n")
    print(batao)
    answer = int(input("Please tell what u want to do:"))
    if answer == 1:
         for key, naam in work.items():
             print("\nPress", key, "for", naam, end="")
         decision = int(input("\nwrite here what do you want to do:"))
         print("ok so u want:", work[decision])
         f = open (name[aapkanaam] + work[decision] + ".txt", "a")
         print("1.click y for yes to write  more\n"
               "2.click n for no to not write more\n")
         guess= 'y'
         while(guess != "n"):
               print("please type your input below")
               mytext = input(">>>>::::")
               f.write (""+ str (getdate ()) + "\n"+" : " + mytext + "\n")
               guess = input("please let me know whether you want to add something more to your file with ' y or n ':")
               continue
    elif answer == 2:
        for key, naam in work.items():
            print("\npress", key, "for", naam, end="")
        decision = int(input("\nright here what do you want to do:"))
        print("ok so u want:", work[decision])
        print("u can not make  changes to your report as u choose to retrieve.\n"
              "but once file is created u can make changes by going into it")
        f = open (name[aapkanaam] + work[decision] + ".txt", "a")
    else:
        print("invalid ! you have either not gone according to what was said\n"
              "or else you have used some invalid characters while feeling the forum.\n")
except Exception as e:
       print("sorry!your file cannot be created\n"
             "it seems like you have made a mistake while processing the above forum\n"
             "please fill it up properly the next time\n")
if answer==1:
    print("YOU PRINTED THE FOLLOWING.")
else:
    print("NOTHING NEW HAS BEEN PRINTED.\n")
f = open (name[aapkanaam] + work[decision] + ".txt", "rt")
content=f.read()
print(content)
f.close()
print(Style.RESET_ALL)
print(Fore.RED)
print(Style.BRIGHT)
print(Style.BRIGHT)
print(Style.BRIGHT)
print(Style.BRIGHT)
print("THANK YOU FOR USING OUR HEALTH MANAGEMENT SYSTEM\n"
      "A PRODUCT BY-\n"
      "TIWARI AND CO\n")

print(Style.BRIGHT)
print(Back.RED)
print(Style.BRIGHT)
print(Back.BLACK)
print(Style.BRIGHT)
print(Back.GREEN)
print(Style.RESET_ALL)




print(Style.BRIGHT)
print(Back.RED)
print(Style.BRIGHT)
print(Back.BLACK)
print(Style.BRIGHT)
print(Back.RED)
print(text())
print(Style.RESET_ALL)

