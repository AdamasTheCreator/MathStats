import pandas as pd
import numpy as np

def simulate_stock_data():
    np.random.seed(42) 
    dates = pd.date_range(start='2023-07-01', periods=21, freq='B')
    stock_prices = np.random.randint(50, 200, size=21)  
    stock_data = pd.DataFrame({'Date': dates, 'StockPrice': stock_prices})
    return stock_data

def test_trading_strategy(stock_data, initial_investment, trade_per_week, trade_per_day):
    amount_per_trade = initial_investment / (trade_per_week * trade_per_day)
    max_loss_per_trade = amount_per_trade * 0.2
    max_profit_per_trade = amount_per_trade / 0.8

    total_profit = initial_investment  
    num_trades = trade_per_week * trade_per_day

    for i in range(0, len(stock_data), num_trades):
        week_data = stock_data.iloc[i:i+num_trades]

        for j in range(len(week_data)):
            stock_price = week_data['StockPrice'].iloc[j]

            if stock_price <= max_loss_per_trade:
                total_profit -= max_loss_per_trade
            else:
                total_profit += max_profit_per_trade

    return total_profit

def main():
    initial_investment = 6000
    trade_per_week = 3
    trade_per_day = 4

    play_again = True
    while play_again:
        stock_data = simulate_stock_data()
        total_profit = test_trading_strategy(stock_data, initial_investment, trade_per_week, trade_per_day)

        print(f"Total profit after 3 weeks: ${total_profit:.2f}")
        initial_investment += total_profit
        print(f"Updated initial investment for the next round: ${initial_investment:.2f}")
        print()
        response = input("Do you want to play again? (y/n): ").lower()
        play_again = response == 'y'

if __name__ == "__main__":
    main()
