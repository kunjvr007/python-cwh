print("welcome to the world of math")
a=int(input("enter your first number "))
b=int(input("enter your second number "))
op=input("enter the operation you want to perform(+,-,*,/):")
if (a,b)==(45,53) and op=="*":
    print("the answer is : 555")
elif (a,b)==(56,9) and op=="+":
    print("the answer is : 77")
elif (a,b)==(56,6) and op=="/":
    print("the answer is : 4")
else:
    if op=="+":
        print("the answer is",a + b)
    elif op=="-":
        print("the answer is",a - b)
    elif op == "*":
        print("the answer is", a * b)
    elif op == "/":
        print("the answer is", a / b)





