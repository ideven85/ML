def my_list(*el,index=0):
    """
    >>> my_list(1,2,3,4)
    4
    """
    if not el:
        return index
    return my_list(*el[1:],index=index+1) # Pointless

def varargs(*args,x):
    print(args,x)

def main():
    import doctest
    # import doctest
    print(doctest.testmod(verbose=True))
    my_list([1,2,3,4])
    varargs([1,2,3,4],x=1)

if __name__ == '__main__':
    main()