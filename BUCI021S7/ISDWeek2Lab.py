num=int(input("Enter a number "))
if(num>10):
  print("LARGE")
else:
  print("SMALL")

#1. Note the indentation!
#In Python this is compulsory

#2. Instead print("LARGE") we can insert an arbitary number
#of operations. We will try such an example during the class

#3. The `else' part is not necessary
#You can comment the last two lines and notice the behavior:
#the program will do nothing if the condition is not satisfied.

#4. Exercise: write a program that asks the user to enter two
#numbers A and B. If B is not zero then the program prints A/B
#otherwise it prints "Incorrect input!"

#5. Nested if instructions.
#Let us modify program for part 1 as follows.
#When does this program print "LARGE,VERY LARGE,SMALL,VERY SMALL?  
num=int(input("Enter a number "))
if(num>10):
  if(num<20):  
     print("LARGE")
  else:
     print("VERY LARGE")
else:
  if(num>5):  
    print("SMALL")
  else:
    print("VERY SMALL")

#6 exercise
#Let us call a number GOOD if it is great than or equal to 40 and
#smaller than 50 (that is 40,41,...,49).
#Write a program that asks the user to enter a number and then prints
#GOOD if the number is good and
#BAD otherwise
#The program should use nested IFs
#Then write a program solving the same task but using a logical connective (AND or OR).    

#7 suppose now that the number is good if it is smaller than 20 or
#larger than 80. Write a program that asks the user to enter a number and then prints
#GOOD if the number is good and
#BAD otherwise
#The program should use nested IFs
#Then write a program solving the same task but using a logical connective (AND or OR).  


    

  
