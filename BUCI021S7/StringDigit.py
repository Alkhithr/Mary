#filtering a string out of non-digit symbols
MyStr=input("Enter a string ")
NewStr=""
for i in range(0,len(MyStr)):
   CurStr=MyStr[i]
   if(CurStr.isdigit()):
        print(CurStr)
        NewStr=NewStr+CurStr
print("The only digit substring is ",NewStr)
