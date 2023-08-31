import sys
def main():
    print("Demostration of Command Line Arguments")
    print("Number of Command line arguements are: ", len(sys.argv))
    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv[2])
    print(sys.argv[3])
    print(sys.argv[4])

    print(type(sys.argv[1]))
    print(len(sys.argv))





if __name__ == "__main__":
    main()


#python Command1.py Marvellous 11 12 13 14