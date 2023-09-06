import threading

def small(str1):
  small_count = 0
  for ch in str1:
    if ch.islower():
      small_count += 1
  print("The No of small characters in the string is: ", small_count)
  print("Thread ID: ", threading.current_thread())
  print("Thread Name: ", threading.current_thread().name)

def capital(str1):
  capital_count = 0
  for ch in str1:
    if ch.isupper():
      capital_count += 1
  print("The No of capital characters in the string is: ", capital_count)
  print("Thread ID: ", threading.current_thread())
  print("Thread Name: ", threading.current_thread().name)

def digits(str1):
  digit_count = 0
  for ch in str1:
    if ch.isdigit():
      digit_count += 1
  print("The No of digits in the string is: ", digit_count)
  print("Thread ID: ", threading.current_thread())
  print("Thread Name: ", threading.current_thread().name)

def main():
  str1 = "Hello World! 9767"

  small_thread = threading.Thread(target=small, args=(str1,))
  capital_thread = threading.Thread(target=capital, args=(str1,))
  digits_thread = threading.Thread(target=digits, args=(str1,))

  small_thread.start()
  capital_thread.start()
  digits_thread.start()

  small_thread.join()
  capital_thread.join()
  digits_thread.join()

if __name__ == "__main__":
  main()
