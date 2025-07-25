def calculate_daily_profit_loss(open_price, close_price):
    """
    Calculate the daily profit or loss for a stock based on the opening and closing prices.
    
    Parameters:
    open_price (float): The opening price of the stock for the day.
    close_price (float): The closing price of the stock for the day.
    
    Returns:
    float: The daily profit or loss.
    """
    # Calculate the difference between the closing price and the opening price
    profit_loss = close_price - open_price
    
    return profit_loss