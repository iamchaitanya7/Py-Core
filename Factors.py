def PrintFactors(n):
    for x in range(1, n + 1):
        if n % x == 0: 
            print(x)

def main():
    x = 0
    n = int(input("Enter a Number to get factors: "))
    PrintFactors(n)

if __name__ =="__main__":
    main()