import re
import sys
ip=input("Enter the ip address:")
x=re.split(r'\.',ip)
for i in x:
    if(int(i)<0 or int(i)>255):
        print("Invalid")
        sys.exit(0)
    else:
        print("Valid")
        sys.exit(0)