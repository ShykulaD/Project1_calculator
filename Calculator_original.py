running = True

while running:
    print("1 = Addition")
    print("2 = Subtraction")
    print("3 = Multiplication")
    print("4 = Division")
    print("5 = Exit program")
    cmd = int(input("Enter number : "))
    if cmd == 1:
        print("Addition")
        first = int(input("Enter first number :"))
        second = int(input("Enter second number :"))
        result = first + second
        print(first, "+", second, "=", result)
        #str = '%d + %d = %d' % (first, second, first+second)
        #print(str)
    elif cmd == 2:
        print("Subtraction")
        first = int(input("Enter first number :"))
        second = int(input("Enter second number :"))
        result = first - second
        print(first ,"-" , second , "=" , result)
    elif cmd == 3:
        print("Mmltiplication")
        first = int(input("Enter first number :"))
        second = int(input("Enter second number :"))
        result = first * second
        print(first ,"*" , second , "=" , result)
    elif cmd == 4:
        print("Division")
        first = int(input("Enter first number :"))
        second = int(input("Enter second number :"))
        result = first / second
        print(first ,"/" , second , "=" , result)
    elif cmd == 5:
        print("Quit!")
        running = False


