#Secret Auction Program
print("WELCOME TO THE SECRET AUCTION")
import os
records = {}
finish = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]

        if (bid_amount > highest_bid):
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")

while not finish:
    name = input("Input your name : ")
    price = int(input("Enter your bidding amount : "))
    records[name] = price
    run = input("Are there any other bidders ?Type 'yes' or 'no' ")
    if (run =="no"):
        finish = True
        find_highest_bidder(records)
    elif(run =="yes"):
        os.system('clear')



