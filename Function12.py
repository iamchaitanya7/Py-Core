
#Fucntion defines another function inside it (Inner Function)

def Marvellous(Val1, Val2):               #Data Abstraction example case study achieve
    def Add(Val1, Val2):
        return Val1 + Val2          
    
    Ans = Add(Val1, Val2)           
    return Ans

def main():

    print("Addition is: ", Marvellous(11, 7))

if __name__ == "__main__":
    main()