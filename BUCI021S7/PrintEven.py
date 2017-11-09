#printing the first N even numbers
n=int(input("How many even numbers would you like to print? "))
print("The first ",n," even numbers are")
for i in range (2,2*n+1,2):
     print(i)
