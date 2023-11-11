#here is a normal version of this function
#def enlarge(n):
#    return float(n) * 100



# here is a documented version of the function

def enlarge(n):
    """ This is a docstring.
    This function enlarges a number.
    Pass in n as a parameter (string).
    Returns a larger version of the number (float).
    """
    return float(n) * 100



if __name__ == "__main__":

    x = input("Please input a number: ")
    result = enlarge(x)
    print(result)





