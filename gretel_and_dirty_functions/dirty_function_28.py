def fetch_profile(user_input):
    """
    Evaluates user input as part of a function call using `eval()`, enabling
    execution of arbitrary code if the input is not properly validated. This
    introduces a high risk of code injection attacks.
    """
    return eval(f"get_profile({user_input})")
