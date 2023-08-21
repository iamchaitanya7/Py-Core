def FirstTenEvenNo(num):
    for i in range(1, 11):
        if num % 2 == 0:
            print(num, end=" ")
            num = num + 2
def main():
    num = 2
    FirstTenEvenNo(num)
if __name__ == "__main__":
    main()