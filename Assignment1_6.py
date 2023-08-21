def PositiveNegative(num):
    if num == 0:
        print("Zero")
    elif num >= 1:
        print("Positive Number")
    else:
        print("Negative Number")
def main():
    num = int(input())
    PositiveNegative(num)
if __name__ == "__main__":
    main()