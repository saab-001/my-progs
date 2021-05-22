while 1==1:
    a=input("enter a number: ")
    b=input("enter another number: ")
    c=input("multiply, subtract, divide, add:")
    multiply_=float(a)*float(b)
    subtract_=float(a)-float(b)
    divide_=float(a)/float(b)
    add_=float(a)+float(b)
    if c==("multiply") or ("*"):
        print(multiply_)
    elif c==("subtract") or ("-"):
        print(subtract_)
    elif c==("divide") or ("/"):
        print(divide_)
    elif c==("add") or ("+"):
        print(add_)
    else :
        print("invalid input")
