class Demo:
    def __init__(self, val1, val2):       #Constructor  aslo called as #instance method
        print("Inside Init")
        self.No1 = val1                     #Instance Variable
        self.No2 = val2

    def Display(self):                           #Instance Method
        print("Value of No1: ", self.No1)
        print("Value of No2: ", self.No2)

def main():
    print("Demo of OOP")
    obj1 = Demo(10, 20)               #__init__(10,20)
    obj2 = Demo(11, 21)               #__init__(11,21)
 
    obj1.Display()
    obj2.Display()

if __name__ == "__main__":
    main()

#main()    we can also call main() method like this also but in single first of python it is effiecnt not in case of many module import