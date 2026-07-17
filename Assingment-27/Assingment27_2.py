class BankAccount:
    ROI = 10.5

    def __init__(self,name,amount):
        self.Name = name
        self.Amount = amount
    def Display(self):
        print(f"Account holder's name {self.Name} and amount is {self.Amount}")
    def Deposit(self,deposit_amount):
        self.Amount = self.Amount + deposit_amount
    def Withdraw(self,withdraw_amount):
        if(withdraw_amount < self.Amount):
            print("Insufficient Balance")
        else:
            self.Amount = self.Amount - withdraw_amount
    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest
    
obj1 = BankAccount("Mani", 10000)
obj2 = BankAccount("Nikita", 5000)

print("----- Account 1 -----")
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.Display()
print("Interest :", obj1.CalculateInterest())

print()

print("----- Account 2 -----")
obj2.Display()
obj2.Deposit()
obj2.Withdraw()
obj2.Display()
print("Interest :", obj2.CalculateInterest())