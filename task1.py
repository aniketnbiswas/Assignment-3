def fact(i):
    n=1
    for i in range(1,i+1):
        n*=i
    print(f"Factorial of {i} is : {n}")
a=int(input("Enter a number: "))
fact(a)