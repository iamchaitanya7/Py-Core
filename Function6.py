#Function Accepts Multiple Parameters and Return Multiple Paramters

def Marvellous(Val1, Val2):
    Addition = Val1 + Val2
    Substraction = Val1 - Val2
    Multiplication = Val1 * Val2
    Division = Val1 / Val2

    return Addition, Substraction, Multiplication, Division

def main():
    Ret = Marvellous(11, 6)
    print(type(Ret))
    print("Addition: ", Ret[0])
    print("Substraction: ", Ret[1])
    print("Multiplication: ", Ret[2])
    print("Division: ", Ret[3])

if __name__ == "__main__":
    main()