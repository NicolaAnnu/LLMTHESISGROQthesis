def calculate_portfolio_value(stock_names, stock_values):
    """
    Calculates the total value of an investment portfolio.

    Parameters:
    stock_names (list): A list of stock names.
    stock_values (list): A list of stock values corresponding to the stock names.

    Returns:
    float: The total value of the investment portfolio.
    """
    if len(stock_names) != len(stock_values):
        raise ValueError("The length of stock_names and stock_values must be the same.")
    
    total_value = 0
    for value in stock_values:
        total_value += value
    
    return total_value