import MarvellousNum

def ListPrime(num_list):
    prime_sum = 0
    for num in num_list:
        if MarvellousNum.ChkPrime(num):
            prime_sum += num
    return prime_sum

def main():
    N = int(input("Enter the number of elements: "))
    num_list = []
    for i in range(N):
        num = int(input())        
        num_list.append(num)
    print("Sum of prime no: ", ListPrime(num_list) )

if __name__ == "__main__":
    main()