from replit import clear
import art

print(art.logo)

auction = []

while True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    auction.append({"name": name, "bid": bid})

    proceed = input("Do you wish to continue? (y/n) ")
    if proceed == "n":
        break
    else:
        clear()


max_bid = 0
max_bidder = ""

for item in auction:
    if item["bid"] > max_bid:
        max_bid = item["bid"]
        max_bidder = item["name"]

print(f"The highest bid is {max_bid} by {max_bidder}.")
