def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a>-10000 and a<-1000 or a>10000 and a>1000
print(main(36165))