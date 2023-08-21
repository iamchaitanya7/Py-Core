def ChkNum(num):
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
def main():
    num = int(input("Enter a Number: "))
    ChkNum(num)
if __name__ == "__main__":
    main()