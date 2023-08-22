def FactorsAdditions(num, factors_sum):
    for i in range(1, num):
        if num % i == 0:
            factors_sum += i
    print(factors_sum)
def main():
        num = int(input())
        factors_sum = 0
        FactorsAdditions(num, factors_sum)
if __name__ == "__main__":
    main()
