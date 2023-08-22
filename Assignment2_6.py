def StartPattern1(num):
    for i in range(num + 1, 0, -1):    
        for j in range(0, i - 1):  
            print("*", end=' ')  
        print(" ")  
def main():
    num = int(input())  
    StartPattern1(num)
if __name__ == "__main__":
    main()
