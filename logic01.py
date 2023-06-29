def main(a,b,c):
    """
    Given three integers a, b, c,  check the following statement "The number b is between a and c".
    Args:
        a(int): parameter a
        b(int): parameter b
        c(int): parameter c
    Returns:
        bool: answer
    """
    x1 = a<b and b<c
    x2 = c<b and b<a
    

    return x1 or x2
print(main(3, 4, 5))