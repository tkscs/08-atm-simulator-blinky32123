"""
Options:
- check the balance: prints current balance
- withdraw money:
    ask you how much to withdraw
    reduce the balance by that amount
    if you try to withdraw more than you have...
        print error don't update the balance
    don't withdraw a negative amount
- deposit money:
    ask you how to deposit
    increase the balance by that amount
    don't deposit a negative amount
- loop (with a while loop) until the user says "exit"
"""
# start with 1 million dollars

balance=1000000

while balance >= 0:
    x = input("would you like to withdraw, deposit, checkbalance, or exit:")
    print(x)
    if x == "withdraw": 
        withdraw =int(input("how much would you like to withdraw "))
        balance = balance - withdraw
        print( "your new balance is: ", balance)
    elif x == "deposit":
        deposit = int(input("how much would you like to deposit"))
        balance = balance + deposit
        print( "your new balance is: ", balance)
    elif x == "checkbalance":
        print("your balance is:", balance) 
    elif x == "exit":
        break
    if balance<0:
        print("BANKRUPT")