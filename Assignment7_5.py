import threading

def thread1():
  for i in range(1, 51):
    print(i)

def thread2():
  for i in range(50, 0, -1):
    print(i)

def main():
  thread1_obj = threading.Thread(target=thread1)
  thread2_obj = threading.Thread(target=thread2)

  thread1_obj.start()
  thread1_obj.join()
  
  thread2_obj.start()
  thread2_obj.join()

if __name__ == "__main__":
  main()
