def ListAddition(num_list, no):
    List_sum = 0
    for i in range(no):
        List_sum = List_sum + num_list[i]
    return List_sum

def main():
    no = int(input("Enter Number of elements: "))
    num_list = []
    for i in range(no):
        num = int(input())
        num_list.append(num)
    print(ListAddition(num_list, no))

if __name__ == "__main__":
    main()