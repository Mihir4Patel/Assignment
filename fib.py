
#for loop
def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
fib(10)

#while loop
n1=int(input("Enter the first number of the series: "))
n2=int(input("Enter the second number of the series: "))
n=int(input("Enter the number of terms needed: "))
print(n1,n2,end=" ")
while(n-2):
    t=n1+n2
    n1=n2
    n2=t
    print(n2,end=" ")
    n=n-1

#recursion loop
def recursion_fib(num):
   if num <= 1:
       return num
   else:
       return(recursion_fib(num-1) + recursion_fib(num-2))
n = 9
if n <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print(recursion_fib(i))
