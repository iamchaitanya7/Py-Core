def DivisibleFive(num):
    if num % 5 == 0:
        print("True")
    else:
        print("False")
def main():
    num = int(input())
    DivisibleFive(num)
if __name__ == "__main__":
    main()