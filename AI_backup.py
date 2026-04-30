from datetime import datetime, date
import os

def make_file():
    a = input("file name ? ")
    os.system("nano " + a)

def pkginstall():
    b = input("pkg name ? ")
    os.system("pkg install " + b)

while True:
    user = input("Command: ").lower()

    if user == "edit ai":
        os.system("nano AI.py")
    elif user == "time":
        print(datetime.now().strftime("%H:%M:%S"))
    elif user == "date":
        print(date.today())
        os.system("help")
    elif user == "help":
        print("Commands:")
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
        print("system shutdown")
        break
    else:
        print("Error — something went wrong")
