#Math

#Porpotion
#n1/d1 = n2/d2
#example => n1/d1 = n2/x => what is x?

import re

def propotion(a,b,c,d):
    n1 = a
    d1 = b
    n2 = c
    d2 = d
    if n1 == "x":
        x1 = (n2/d2)*d1
        print("x = ",x1)
    if d1 == "x":
        x2= n1/(n2/d2)
        print("x = ",x2)
    if n2 == "x":
        x3=(n1/d1)*d2
        print("x = ",x3)
    if d2 == "x":
        x4= (n2/(n1/d1))
        print("x = ",x4)
    
userinput = input("Get x of an porpotion equation( ex: x/3=2/4): ")
parts = userinput.replace(" ", "").split("=")
string_uknown = "x"
if string_uknown in parts[0]:
    parts2 = parts[0].split("/")
    parts3 = parts[1].split("/")
    if parts2[0] == "x":
        
        d1 = re.findall(r'\d+',parts[0])[0]
        n2 = parts3[0]
        d2 = parts3[1]
        propotion("x",int(d1),int(n2),int(d2))
    if parts2[1] == "x":
        n1 = re.findall(r'\d+',parts[0])[0]
        n2 = parts3[0]
        d2 = parts3[1]
        propotion(int(n1),"x",int(n2),int(d2))
if string_uknown in parts[1]:
    parts5 = parts[0].split("/")
    parts4 = parts[1].split("/")
    if parts4[0] == "x":
        d2 = re.findall(r'\d+',parts[1])[0]
        n2 = parts4[0]
        n1 = re.findall(r'\d+',parts[0])[0]
        d1 = parts5[1]
        propotion(int(n1),int(d1),"x",int(d2))
    if parts4[1] == "x":
        d2 = parts4[1][0]
        n2 = parts4[0]
        n1 = re.findall(r'\d+',parts[0])[0]
        d1 = parts5[1]
        propotion(int(n1),int(d1),int(n2),"x")
        

