def main(a,b):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is positive".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    x1 = a%2==1
    x2 = b%2==1
    
    return x1 or x2
print(main(6,-4))