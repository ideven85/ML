def my_list(*el):
    """
    >>> my_list(1,2,3,4)
    4
    """
    if not el:
        return 0
    return 1+my_list(*el[1:])

