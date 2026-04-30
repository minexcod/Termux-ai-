import os
from datetime import datetime, date

while True:
    user = input("command: ").lower()
    
    if user == "hi":
        print("hi")
    elif user == "time":
        print(datetime.now().strftime("%H:%M:%S"))
    elif user == "date":
        print(date.today())
    elif user == "bye":
        print("bye")
        break
    else:
        print("command nahi pehchana")
