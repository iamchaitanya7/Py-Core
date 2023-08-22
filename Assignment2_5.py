def PrimeNumber(num, flag):
    for i in range(2,num):
        if num%i==0:
            flag = 1
            break
    if flag == 1:
        print("It is Not a Prime Number")        
    else:
        print("It is a Prime Number")
def main():
    num = int(input())
    flag = 0
    PrimeNumber(num, flag)
if __name__ == "__main__":
    main()