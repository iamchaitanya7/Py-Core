def Display(i):
    if (i<6):
        print(i, end=" ")
        i += 1
        Display(i)

def main():
    Display(1)

if __name__ == "__main__":
    main()