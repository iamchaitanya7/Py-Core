#Function Accepts More Parameter and Return Nothing

def Marvellous(Name, Age, City):
    print("Inside Marvellous Function")
    print("Welcome: ", Name)
    print("Age: ", Age)
    print("City: ", City)

def main():
    Marvellous("Chaitanya", 21, "Pune")
    Marvellous(City = "Mumbai", Age = 30, Name = "Bhaiya")

if __name__ == "__main__":
    main()