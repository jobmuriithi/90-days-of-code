#ENCAPSULATION AND ACCESS MODIFIERS
#It's keeping the data safe and controlling how it is accessed.
#ATM the inserts a card, enters PIN, withdraws money

#ACCESS MODIFIERS
#3 types  PUblic members, Protected members, Private members

#PUBLIC MEMBERS
#They are available everywhere

class Student:
    def __init__(self):
        self.name = "JOB"

student = Student()
print(student.name)

#PROTECTED MEMBERS
#They begin with one undescore
class Bank:
    def __init__(self):
        self._balance = 900

bank = Bank()
print(bank._balance)

#PRIVATE MEMBERS
#They begin with two undescores
class Bank:
    def __init__(self):
        self.__balance = 1000

bank = Bank()
print(bank.__balance)


#METHOD CONTROL DATA

#GETTERS AND SETTERS
#You might want to update private data safely
#Getters read the value

def get__balance(self):
    return self.__balance

print(account.get__balance)

#Setters update the value after validation

def set__balance(self,amount):
    if amount >= 0:
        self.__balance = amount

    else:
        print("Invalid amount!!!")




