def main():
    L = int(input("Enter No of elements to insert into list: "))
    arr = list()

    print("Enter Elements")
    for i in range(L):
        val = input()
        arr.append(val)

    print("Elements of List are: ")
    for i in range(len(arr)):
        print(arr[i])

if __name__ == "__main__":
    main()