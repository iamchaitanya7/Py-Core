def list_frequency(num_list, num_freq):
    frequency = 0
    for i in num_list:
        if i == num_freq:
            frequency += 1
    return frequency

def main():
    n = int(input("Enter the number of elements: "))
    num_list = []
    for i in range(n):
        num = int(input())
        num_list.append(num)
    num_freq = int(input("Element to find frequency: "))
    print("Element Frequency: ",list_frequency(num_list, num_freq))
    
if __name__ == "__main__":
    main()