#computing Fibonacci numbers
n=int(input("Enter a number n for which you want to compute F(n) "))
if(n<=2):
     print("The number is 1")
else:
  #initialization of F(n-1) and F(n-2) for n=3
  FibPrev=1
  FibBefPrev=1
  for i in range (3,n+1):
       #Computing F(i)
       NewFib=FibPrev+FibBefPrev
       if(i<n):
          FibBefPrev=FibPrev
          FibPrev=NewFib
  print("The number is ",NewFib) 
