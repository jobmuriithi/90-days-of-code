class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance

        #Getter
    def get_balance(self):
        return self.__balance

        #Setter
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount

        else:
            print("Balance cannot be negative")

account = BankAccount("Job", 50000)

#Using the getter
print(account.get_balance())

#Using the setter
print(account.set_balance())

account.set_balance(-1000)

print(account.get_balance())


#Reading line by line
file = open("grade_calculator.py","r")

for line in file:
    print(line)

file.close()
