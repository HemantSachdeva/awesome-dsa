def main(num):
    """
    repeteadly add the digits of a number until it becomes a single digit
    """
    # convert to string
    num = str(num)
    # base case: if length of number is 1, return the number
    if len(num) == 1:
        return num
    # recursive case: if length of number is greater than 1, add the digits
    # and call the function again
    else:
        # add the digits
        total = 0
        for i in num:
            total += int(i)
        # call the function again
        return main(total)
