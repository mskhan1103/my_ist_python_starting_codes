def calculator(num1,num2,op):
    x=0
    if op == "+" :
       x=num1+num2
    elif op=="-":
       x=num1-num2
    elif op=="*":
       x=num1*num2
    elif op=="/":
       x=num1/num2
    else:
       x="you have entered wrong op please check."

    return x

num1=int(input("Enter your ist no ."))
num2=int(input("Enter your 2nd no ."))
op=(input("Enter your op  ."))
    
result=calculator(num1,num2,op)
print(result)

      
    
    