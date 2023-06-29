def main(a,b):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is even".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    x1 = a%2==0
    x2 = b%2==0
    answer = x1 and x2
    return answer
print(main(6,4))