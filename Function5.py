#Function Accepts Multiple Parameters and Return Multiple Paramters

def Marvellous(Val1, Val2):
    Addition = Val1 + Val2
    Substraction = Val1 - Val2
    Multiplication = Val1 * Val2
    Division = Val1 / Val2

    return Addition, Substraction, Multiplication, Division

def main():
    Ret1, Ret2, Ret3, Ret4 = Marvellous(11, 6)
    print("Addition: ", Ret1)
    print("Substraction: ", Ret2)
    print("Multiplication: ", Ret3)
    print("Division: ", Ret4)

if __name__ == "__main__":
    main()