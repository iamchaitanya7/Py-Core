
class Arithmetic:
    def __init__(self,A,B):
        print("Inside Constructor")
        self.No1 = A
        self.No1 = B

    def Addition(self):
        Ans = 0
        Ans = self.No1 + self.No2
        return Ans
    
    def Substraction(self):
        Ans = 0
        Ans = self.No1 - self.No2
        return Ans

def main():
    val1 = int(input("Enter First Number: "))
    val2 = int(input("Enter Second Number: "))

    obj1 = Arithmetic(val1, val2)                #object 1

    Ret = obj1.Addition()
    print("Addition is: ", Ret)

    Ret = obj1.Addition()
    print("Substraction is: ", Ret)



    obj2 = Arithmetic(val1, val2)                 #object 2

    Ret = obj2.Addition()
    print("Addition is: ", Ret)

    Ret = obj2.Addition()
    print("Substraction is: ", Ret)

if __name__ == "__main__":
    main()