
def Add(Val1, Val2):
    return Val1 + Val2

#def Sub(Val1, Val2):
#   return Val1 - Val2

#Fucntion Accepts parameters as Another Function
def Marvellous(FPTR1):                #FTPR1 is consider as a Function parameter name which accepts the function as input *** basically its ***Function Pointer***
    print(type(FPTR1))
    Ans = FPTR1(11, 7)
    print("Addition is: ", Ans)

def main():
    Marvellous(Add)
    
if __name__ == "__main__":
    main()