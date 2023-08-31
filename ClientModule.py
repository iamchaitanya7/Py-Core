import Module

def main():
    val1 = int(input("Enter First Number : "))
    val2 = int(input("Enter Second Number : "))
    result = 0

    result = Module.Addition(val1, val2)
    print("Addition is : ", result)

    result = Module.Substraction(val1, val2)
    print("Substraction is : ", result)

    result = Module.Multiplication(val1, val2)
    print("Multiplication is : ", result)

    result = Module.Division(val1, val2)
    print("Division is : ", result)

if __name__ == "__main__":
    main()
