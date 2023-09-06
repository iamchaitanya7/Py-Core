import threading

def even_factors(number):
  sum_even_factors = 0
  for i in range(2, number):
    if number % i == 0:
      sum_even_factors += i
  print("The sum of even factors of is: ", sum_even_factors)

def odd_factors(number):
  sum_odd_factors = 0
  for i in range(1, number):
    if number % i == 0 and i % 2 == 1:
      sum_odd_factors += i

  print("The sum of odd factors of is: ", sum_odd_factors)

def main():
  number = int(input("Enter a number: "))

  even_thread = threading.Thread(target=even_factors, args=(number,))
  odd_thread = threading.Thread(target=odd_factors, args=(number,))

  even_thread.start()
  odd_thread.start()

  even_thread.join()
  odd_thread.join()

  print("Exit from main")

if __name__ == "__main__":
  main()
