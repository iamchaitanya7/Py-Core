#Function Accepts Parameters and Call Another Function from It....

def Add(Val1, Val2):
    return Val1 + Val2

def Sub(Val1, Val2):
    return Val1 - Val2

def Marvellous(Val1, Val2):
    Ans = Add(Val1, Val2)
    print("Addition is: ", Ans)
    Ans = Sub(Val1, Val2)
    print("Substraction is: ", Ans)

def main():
    Marvellous(11, 7)
    
if __name__ == "__main__":
    main()