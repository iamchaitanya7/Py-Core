from functools import reduce

def main():
    num_list = []
    n = int(input("Enter Number of elements: "))
    for i in range(n):
        num = int(input())
        num_list.append(num)
    filterX = list(filter(lambda num : (num % 2 == 0), num_list))
    mapX = list(map(lambda num : (num ** 2), filterX))
    reduceX = reduce(lambda x, y : (x + y), mapX) 
    print("List after filter = ", filterX)
    print("List after Map = ", mapX)
    print("Output after reduce = ", reduceX)

if __name__ == "__main__":
    main()