def main(a,b,c):
    """
    Find how many negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    len=0
    if a<0:
        len+=1
    if b<0:
        len+=1
    if c<0:
        len+=1

    return len
print(main(12,45,-54))