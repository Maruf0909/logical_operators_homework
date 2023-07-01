def main(x):
    """
    Given a two digit integer x, return true if x is palindrome integer.
    An integer is a palindrome, when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    d1 = x % 10
    x = x // 10
    d2 = x % 10
    x = x // 10
    
    return d1 == d2
print(main(33)) 
