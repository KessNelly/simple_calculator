
def user():
    num1 = int(input("choose a number: "))
    num2 = int(input("choose a second number: "))
    operator = input("choose an operator amongst the following +,-,*,/ : ")

    if operator == "+" :
        return num1 + num2
    
    elif operator == "-" :
        return num1 - num2
    
    elif operator == "*" :
        return num1 * num2
    
    elif operator == "/" :
        if num2 == 0:
            return f"{num1} is not divisible by {num2}"
        else:
            return num1 / num2
     
    else:
        return f"invalid operator!!!"
    
print(user())

