def best_profit(stock_prices):
    """Calculates the best possible profit from buying and selling. Checks for lowest loss as well.

    Input: List of stock prices.
    Output: Float, max possible profit for the day.
    """

    if len(stock_prices) < 2:

        raise ValueError("Getting a profit requires at least 2 prices.")

    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for current_time in xrange(1, len(stock_prices)):
        current_price = stock_prices[current_time]

        potential_profit = current_price - min_price

        max_profit = max(max_profit, potential_profit)

        min_price = min(min_price, current_price)

    return max_profit