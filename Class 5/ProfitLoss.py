buying_price = float(input("Enter the buying price of oranges: "))
selling_price = float(input("Enter the selling price of oranges: "))

if selling_price > buying_price:
    profit = selling_price - buying_price
    print("You made a profit of {} taka.".format(profit))
elif selling_price < buying_price:
    loss = buying_price - selling_price
    print("You incurred a loss of {0} taka.".format(loss))
else:
    print("No profit, no loss.")
