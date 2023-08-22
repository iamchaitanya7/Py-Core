def FactorialNumber(num, factorial):
    for i in range(1,num + 1):
        factorial = factorial*i
    print(factorial)
def main():
    num = int(input())
    factorial = 1
    FactorialNumber(num, factorial)
if __name__ == "__main__":
    main()
