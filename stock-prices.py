def best_profit(stock_prices):
    """Calculates the best possible profit from buying and selling. Checks for lowest loss as well.

    Input: List of stock prices.
    Output: Float, max possible profit for the day.
    """

    if len(stock_prices) < 2:

        raise ValueError("")

    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for current_price in stock_prices:

        