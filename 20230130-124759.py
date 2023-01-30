#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str);
nationality = input("enter the nationality").lower()
age = int(input("enter age"))
if age == 18 and nationality == "kenyan":
    print("eligible to vote")
else:
    print("not eligible to vote")