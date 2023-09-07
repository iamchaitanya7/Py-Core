class BankAccount:
    ROI = 10.5 
    
    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount

    def Deposit(self, amount):
        self.Amount = self.Amount + amount
        print("Amount Deposited Successfully.....")
    
    def Withdraw(self, amount):        
        if self.Amount < amount:
            print("There is insufficent Balance")
        else:
            self.Amount = self.Amount - amount
            print("Amount Withdrawal Successfully.....")
    
    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print("Interest on account: ", interest)

    def Display(self, ):
        print("Name: ", self.Name)
        print("Balance: ",self.Amount)

def main():
    John = BankAccount("John", 5000)
    Alice = BankAccount("Alice", 8000)

    John.Deposit(2000)
    John.Withdraw(1000)
    John.CalculateInterest()
    John.Display()

    Alice.Deposit(1000)
    Alice.Withdraw(2500)
    Alice.CalculateInterest()
    Alice.Display()

if __name__ == "__main__":
    main()