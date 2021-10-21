def calc():
    print("""1)add
2)sub
3)multiplication
4)division""")
    a=int(input("Choice of operation:"))
    b=int(input("first number:"))
    c=int(input("second number:"))
    if a==1:
        print("Answer:",b+c)
    if a==2:
        print("Answer:",b-c)
    if a==3:
        print("Answe:",b*c)
    if a==4:
        print("Answer:",b/c)


calc()
