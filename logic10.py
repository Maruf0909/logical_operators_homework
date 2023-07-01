def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    
    
    return a>-100 and a<-9 or a>9 and a<100
print(main(23))