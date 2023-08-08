def calculate_trade_details():
    try:
        print()
        # Get user input for the total amount of money
        amount_of_money = float(input("Enter the total amount of money: $"))

        # Calculate amount per trade and profit per trade
        amount_per_trade = amount_of_money / 12
        profit_per_trade = amount_per_trade * 0.1

        # Print the output
        print(f"You need to trade with ${amount_per_trade:.2f} per trade.")
        print(f"You need to make ${profit_per_trade:.2f} profit per trade.")
    except ValueError:
        print("Invalid input. Please enter a valid amount of money.")

if __name__ == "__main__":
    while True:
        calculate_trade_details()
        user_input = input("Type 'exit' to quit or press Enter to calculate again: ")
        if user_input.lower() == "exit":
            break
