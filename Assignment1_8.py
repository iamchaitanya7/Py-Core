def StarPattern(num):
    for i in range(num):
        print("*", end =" ")
def main():
    num = int(input())
    StarPattern(num)
if __name__ == "__main__":
    main()