class Numbers:
    def __init__(self, value):
        self.Value = value
    
    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value)):
            if self.Value % i == 0:
                return False
        return True
    
    def ChkPerfect(self):
        return self.SumFactors() == self.Value
    
    def Factors(self):
        factors = []
        for i in range(1, self.Value):
            if self.Value % i == 0:
                factors.append(i)
        return factors
    
    def SumFactors(self):
        return sum(self.Factors())
def main():
    num1 = Numbers(7)
    print("Prime No : ", num1.ChkPrime())
    print("Perfect No : ", num1.ChkPerfect())
    print("Factors : ",num1.Factors())
    print("Sum of factors : ",num1.SumFactors())

    num2 = Numbers(28)
    print("Prime No : ", num2.ChkPrime())
    print("Perfect No : ", num2.ChkPerfect())
    print("Factors : ",num2.Factors())
    print("Sum of factors : ",num2.SumFactors())

if __name__ == "__main__":
    main()