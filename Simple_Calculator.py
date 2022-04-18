while True:
    num1=int(input("Enter The First Number:-"))
    oper=input("Enter The Operation:-")
    num2=int(input("Enter The Second Number:-"))
    if oper=="+":
        sum=num1+num2
        print("The Answer is:-",sum)
    elif oper=="-":
        sub=num1-num2
        print("The Answer is:-",sub)
    elif oper=="*":
        multi=num1*num2
        print("The Answer is:-",multi)
    elif oper=="/":
        div=num1/num2
        print("The Answer is",div)
        
    else:
        print("Wrong Operation Input:-")
    print("=========================================\n")