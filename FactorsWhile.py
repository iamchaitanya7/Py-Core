def PrintFactors(n):
    while x <= n:
        if n % x == 0: 
            print(x)
            x = x + 1

def main():
    x = 0
    n = int(input("Enter a Number to get factors: "))
    PrintFactors(n)

if __name__ =="__main__":
    main()