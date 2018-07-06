def get_max_profit(stock_prices):

    if len(stock_prices) < 1:
        raise ValueError
    max_profit = stock_prices[1] - stock_prices[0]
    current_min_price = stock_prices[0]
    for i in range(1,len(stock_prices)):
        profit = stock_prices[i] - current_min_price
        if stock_prices[i] < current_min_price:
            current_min_price = stock_prices[i]
        if profit > max_profit:
            max_profit = profit
    return max_profit