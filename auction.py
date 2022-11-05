import os
from art import logo
def clear(): return os.system("cls")
# HINT: You can call clear() to clear the output in the console.


print(logo)
print("Welcome to the secret auction program.")
bidders = {}
other_bidders = True

while other_bidders:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    other_bidders = True

    bidders[name] = bid
    more_bids = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if more_bids == "no":
        other_bidders = False

    if other_bidders:
        clear()

clear()
winning_bid = 0
winner = ""
for bidder in bidders:
    if bidders[bidder] > winning_bid:
        winning_bid = bidders[bidder]
        winner = bidder

print(f"The winner is {winner} with a bid of ${winning_bid}")
