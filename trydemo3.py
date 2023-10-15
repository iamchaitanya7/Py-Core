def main():

    print("Enter First No")
    no1 = int(input())

    print("Enter Second No")
    no2 = int(input())

    ans = 0

    try:
        ans = no1 / no2

    except Exception as zobj:
        print("Exception occured: ", zobj)
        return

    print("Division is: ", ans)

if __name__ == "__main__":
    main()