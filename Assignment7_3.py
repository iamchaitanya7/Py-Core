import threading

def evenlist(nums):
  even_sum = 0
  for i in nums:
    if i % 2 == 0:
      even_sum += i
  print("The sum of even numbers is", even_sum)

def oddlist(nums):
  odd_sum = 0
  for i in nums:
    if i % 2 == 1:
      odd_sum += i
  print("The sum of odd numbers is", odd_sum)

def main():
  nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  even_thread = threading.Thread(target=evenlist, args=(nums,))
  odd_thread = threading.Thread(target=oddlist, args=(nums,))

  even_thread.start()
  odd_thread.start()

  even_thread.join()
  odd_thread.join()

if __name__ == "__main__":
  main()
