# Task 2: Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

stock_name = input("Enter stock name (AAPL, TSLA, GOOGL, MSFT, AMZN): ").upper()

if stock_name in stock_prices:
    quantity = int(input("Enter the number of shares: "))

    if quantity > 0:
        price = stock_prices[stock_name]
        total_investment = price * quantity

        print("\n----- Stock Portfolio Summary -----")
        print("Stock Name:", stock_name)
        print("Price per Share: $", price)
        print("Quantity:", quantity)
        print("Total Investment: $", total_investment)
    else:
        print("Please enter a quantity greater than zero.")
else:
    print("Stock not found. Please enter a valid stock name.")