def addition(No1, No2):
    result = 0
    result = No1 + No2
    return result

def main():
    val1 = int(input("Enter First Number :"))
    val2 = int(input("Enter Second Number :"))
    ans = 0
    ans = addition(val1, val2)
    print("Addition is : ", ans)
if __name__ == "__main__":
    main()