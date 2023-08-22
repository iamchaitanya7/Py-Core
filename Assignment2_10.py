def sum_of_digits(num):
    total_sum = 0
    while num > 0:
        digit = num % 10
        total_sum = total_sum + digit
        num = num // 10
    print(total_sum)
def main():
    num = int(input())
    sum_of_digits(num)
if __name__ == "__main__":
    main()