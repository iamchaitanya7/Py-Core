def PositionalDisplay(Name, Age, Marks):
    print("Name is: ", Name)
    print("Age is: ", Age)
    print("Marks is: ", Marks)

def KeywordDisplay(Name, Age, Marks):
    print("Name is: ", Name)
    print("Age is: ", Age)
    print("Marks is: ", Marks)

def DefaultDisplay(Name, Age, Marks = 100):
    print("Name is: ", Name)
    print("Age is: ", Age)
    print("Marks is: ", Marks)

def VariableDisplay(*values):
    print(type(values))
    print(len(values))
    print(values)

def VariableDisplayLoop(*values):
    for i in range(len(values)):
        print(values[i])


def main():
    #demostration of Positional arguements
    PositionalDisplay("Amit", 25, 90)
    PositionalDisplay("Sagar", 20, 95)

    #demostration of Keyword arguements
    KeywordDisplay(Name = "Amit", Age = 25, Marks = 90)
    KeywordDisplay(Name = "Sagar",Marks = 20, Age = 95)

    #demostration of Default arguements
    DefaultDisplay("Amit", 25)
    DefaultDisplay("Sagar", 20, 95)

    VariableDisplay(10, 20, 30, 40, 50)
    VariableDisplayLoop(11, 21, 33, 44, 55)


if __name__ == "__main__":
    main()