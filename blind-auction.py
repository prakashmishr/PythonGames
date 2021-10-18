logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


from replit import clear

print(logo)
print("welcome to Blind Auction")

bids = {}
bidding = True

def highest(bid):
  highest = 0
  for bidder in bid:
     high = bid[bidder]
     if highest < high:
       highest = high
  print(f"the {bidder} is winner with Rs{highest}")     



while bidding :
    name = input("enter name: ")
    price = int(input("enter bid amount: Rs"))
    bids[name] = price
    bidder =input("Another Bidder? y/n \n")
    if bidder == "n":
      #print(bids)
      highest(bids)
      bidding = False
    elif bidder == "y":
      #print(bids)
      bidding = True 
      clear() 
