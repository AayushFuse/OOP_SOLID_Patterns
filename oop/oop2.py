"""
Build a Python class to represent a simple banking system. 
Create a class for a BankAccount, and another for Customer. 
The BankAccount class should have a constructor to initialize the account details (account number, balance, account type). 
The Customer class should have a constructor to set the customer's details (name, age, address) and create a BankAccount object for each customer. 
Implement a destructor for both classes to display a message when objects are destroyed.
"""

class BankAccount:
    def __init__(self,account_no,balance,account_type) -> None:
        self.__account_no = account_no
        self.__balance = balance
        self.__account_type = account_type

    def __del__(self):
        print(f"{self.__account_no} is destroyed") 

    @property
    def account_no(self):
        return self.__account_no

class Customer:
    def __init__(self,name,age,address,bank) -> None:
        self.name = name
        self.age = age
        self.address = address
        self.bank = bank

    @property
    def bank_account(self):
        return self.bank.account_no
    
    @bank_account.setter
    def bank_account(self,bank):
        self.bank = bank

    def __str__(self):
        return f"Customer Name: {self.name}\nAge: {self.age}\nAddress: {self.address}\nAccountNo: {self.bank_account}"
    
    def __del__(self):
        print(f"{self.name} object is destroyed") 

if __name__=="__main__":
    acc = BankAccount("0107010016967",90000,"Saving")
    cus1 = Customer("Aayush",22,"Dhapasi",acc)
    cus1.bank_account = acc
    print(cus1)

