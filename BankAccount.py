"""
This project will be
all about bank acount.
writer: Dongyun Cho from S.Korea
"""

print "Welcome to Bankworld."
class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
    
  def __repr__(self):
    return "%s's Bankaccount has %.2f"\
  % (self.name, self.balance) #6 What is $????????????
  
  def show_balance(self): 
    print "Balance:%.2f" %self.balance
  
  def deposit(self, amount):
    self.amount = amount
    if amount <= 0:
      print "Error! Invaild amount"
      return
    else:
      print "%.2f is accepted in your account" % self.amount
      self.balance += amount #11
      self.show_balance()# 13?????last sentence
  
  def withdraw(self, amount):
    self.amount = amount
    if amount>self.balance:
      print "Error! You put more than balance"
      return
    else:
      print "You're withdrawing %.2f." %self.amount
      self.balance -= amount
      self.show_balance()
  
my_account = BankAccount("Dongyun")
print my_account
my_account.show_balance() # ~~~~~T_T
my_account.deposit(-22)
my_account.withdraw(1000)
print my_account