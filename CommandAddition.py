import sys
def main():
    print("Addition of Command Line Arguments")

    val1 = int(sys.argv[1])
    val2 = int(sys.argv[2])
    #ans = val1 + val2

    print("Addition is: ", val1 + val2)

if __name__ == "__main__":
    main()


#python Command1.py Marvellous 11 12 13 14