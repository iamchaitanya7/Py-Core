def list_find_maximum(num_list):
    maximum = num_list[0]
    for i in num_list:
        if i > maximum:
            maximum = i
    return maximum

def main():
    n = int(input("Enter Number of elements: "))
    num_list = []
    for i in range(n):
        no = int(input())
        num_list.append(no)
    print("Maximum number:", list_find_maximum(num_list))

if __name__ == "__main__":
    main()