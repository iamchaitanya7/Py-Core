def NumberPattern1(n):
    for i in range(n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
def main():
    n = int(input())
    NumberPattern1(n)
if __name__ == "__main__":
    main()