from datetime import datetime, date
import os

def make_file():
    try:
        a = input("file name ? ")
        if a == "":
            print("firs give me a name")
        else:
            os.system("nano " + a)
    except:
        print("SOMETHING WENT WRONG!")

def pkginstall():
    try:
        b = input("pkg name? ")
        if b == "":
            print("firs give me a name")
        else:
            os.system("pkg install " + b)
    except:
        print("SOMETHING WENT WRONG!")

while True:
    user = input("Command: ").lower().strip()

    f = open("log.txt","a")
    f.write(user + "\n")
    f.close()

    if user == "edit ai":
        os.system("nano AI.py")
    elif user == "time":
        print(datetime.now().strftime("%H:%M:%S"))
    elif user == "date":
        print(date.today())
    elif user == "help":
        print("time - current time")
        print("date - current day")
        print("edit ai - edit assistant")
        print("exit - u exit for the assistant")
        print("install - u can install pkg")
        print("clr - clear")
        print("file - u can make new file or edit the file")
    elif user == "file":
        make_file()
    elif user == "clr":
        os.system("clear")
    elif user == "install":
        pkginstall()
    elif user == "update":
        os.system("apt update && apt upgrade ")
    elif user == "exit":
        print("SYSTEM SHUTDOWN")
        break
    else:
        print("ERROE — SOMETHING WENT WRONG")
