import sys
i = 1

def Display(no):
    global i
    if (i <= no):
        print(i, end=" ")
        i += 1
        Display(no)

def main():
    n = int(input())
    Display(n)

if __name__ == "__main__":
    main()