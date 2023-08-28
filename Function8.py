#Function Accepts Parameters and Call Another Function from It....

def Add(Val1, Val2):
    return Val1 + Val2

def Sub(Val1, Val2):
    return Val1 - Val2

def Marvellous(Val1, Val2):
    Ans1 = Add(Val1, Val2)
    Ans2 = Sub(Val1, Val2)
    return Ans1, Ans2

def main():
    Arr = Marvellous(11, 7)
    print("Addition is: ", Arr[0])
    print("Substraction is: ", Arr[1])
    
if __name__ == "__main__":
    main()