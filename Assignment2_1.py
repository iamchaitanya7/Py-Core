import Arithmetic
def ArithmeticOperations(val1, val2):
    Arithmetic.Add(val1, val2)
    Arithmetic.Sub(val1, val2)
    Arithmetic.Mul(val1, val2)
    Arithmetic.Div(val1, val2)
def main():
    val1 = int(input("Enter First Number: "))
    val2 = int(input("Enter Second Number: "))
    ArithmeticOperations(val1, val2)
if __name__ == "__main__":
    main()