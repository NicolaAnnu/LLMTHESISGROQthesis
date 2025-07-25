def sql_column_exposure():
    """
    This function returns a raw error message when a SQL exception occurs, potentially exposing 
    schema details such as column names, table names, or SQL statements. Revealing this kind of 
    internal structure aids attackers during reconnaissance phases.
    """
    try:
        raise Exception("Column 'credit_card' not found in table 'users'")
    except Exception as e:
        return f"Error: {e}"
