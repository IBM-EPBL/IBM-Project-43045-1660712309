x = float(input("Enter number1: "))
op = input("Enter operator: ")
y = float(input("Enter number2: "))

def calc(a, b, op):
    if(op == "+"):
        return a+b;
    elif(op == "-"):
        return a-b;
    elif(op == "*"):
        return a*b;
    elif(op == "/"):
        return a/b;
    elif(op == "%"):
        return a%b;
    else:
        return "Invalid operation!"

res = calc(x, y, op)
print(x, op, y, " = ", res)