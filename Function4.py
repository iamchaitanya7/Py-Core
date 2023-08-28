#Function Accepts Parameter and Return Paramter

def Marvellous(Val1, Val2):
    if(Val1 > Val2):
        return Val1
    else:
        return Val2

def main():
    print("Largest No: ",Marvellous(10, 20))
    print("Largest No: ",Marvellous(30, 20))

if __name__ == "__main__":
    main()