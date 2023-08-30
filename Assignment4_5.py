from functools import reduce

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def find_maximum(x, y):
    return x if x > y else y

def main():
    num_list = []
    n = int(input("Enter Number of elements: "))
    for i in range(n):
        num = int(input())
        num_list.append(num)

    filterX = list(filter(is_prime, num_list))
    mapX = list(map(lambda num : (num * 2), filterX))
    reduceX = reduce(find_maximum, mapX)

    print("List after Filter = ", prime_nums)
    print("List after Map = ", doubled_primes)
    print("Output of Reduce = ", max_result)
