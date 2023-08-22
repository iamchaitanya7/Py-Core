def NumberPattern(n):
    for i in range(n):
        for j in range(n):
            print(j+1, end= " ")
        print()
def main():
    n = int(input())
    NumberPattern(n)
if __name__ == "__main__":
    main()