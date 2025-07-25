def process_order(quantity):
    """
    Processes an order with the given quantity.
    Vulnerable due to insufficient input validation (no type or range checks).
    """
    if quantity > 0:
        execute_order(quantity) #type: ignore