# track personal expenses
food_money= int (input("food_money"))
print (food_money)
transport_money =int(input("transport_money"))
print (transport_money)
entertainment_money=int(input("entertainment_money"))
print (entertainment_money)
total_expenses = food_money + transport_money + entertainment_money
print (total_expenses)
if total_expenses>=1000:
    print ("exceeds budget")
else:
    print("not exceeded")