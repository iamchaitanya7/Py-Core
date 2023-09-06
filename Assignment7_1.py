import threading

def even_numbers():
    for i in range(20):  
        if i % 2 == 0:
            print("Even:", i)

def odd_numbers():
    for i in range(20): 
        if i % 2 == 1:
            print("Odd:", i)

def main():
    even_thread = threading.Thread(target=even_numbers)
    odd_thread = threading.Thread(target=odd_numbers)

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    print("Both threads have finished.")

if __name__ == "__main__":
    main()
