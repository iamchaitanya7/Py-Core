
def Sub(A, B):
    if (A < B):
        A, B = B, A          #Swapping of numbers in python
    return A - B

def main():
    print("Substraction is: ", Sub(10, 7))
    print("Substraction is: ", Sub(7, 10))

if __name__ == "__main__":
    main()