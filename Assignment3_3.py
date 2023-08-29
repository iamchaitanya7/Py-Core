def list_find_minimum(num_list):
    minimum = num_list[0]
    for i in num_list:
        if i < minimum:
            minimum = i
    return minimum

def main():
    n = int(input("Enter Number of elements: "))
    num_list = []
    for i in range(n):
        no = int(input())
        num_list.append(no)
    print("Minimum number:", list_find_minimum(num_list))

if __name__ == "__main__":
    main()