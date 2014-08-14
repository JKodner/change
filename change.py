def change(num, d1=True, q=True, d=True, n=True, p=True):
    """Returns all combinations of U.S. currency that total up to the given 'num' 
    parameter ('num' is in $1 units).

    Note: 'num' value must be a positive int/float. Else, an error will be returned.

    The parameters include 'd1', 'q', 'd', 'n', 'p', which represent 1 dollar bill, quarter,
    dime, nickel, and penny, respectively. If these values are set to True, then they will
    be included in the combinations. If these values are set to False, then they will not
    be included. If they are set to any other values, an error will be returned.

    This function will return a list, containing the combinations of coins (in a formatted
    list).

    Combination Format:
    [1 Dollar Bills, Quarters, Dimes, Nickels, Pennies]"""

    if not isinstance(num, (int, float)) or (num < 0):
        raise ValueError("'num' value must be positive integer/float.")
    for i in (d1, q, d, n, p):
        if not isinstance(i, bool):
            raise ValueError("Values (d1, q, d, n, p) must be booleans.")
    num = round(num, 2)
    max_penny = round(num * 100)
    nickel_amt = 0
    dime_amt = 0
    quarter_amt = 0
    d1_amt = 0
    if p:
        combs = [[0, 0, 0, 0, int(max_penny)]]
    else:
        combs = []

    for i in range(0, int(max_penny+1))[::-100]:
        if i != max_penny:
            d1_amt += 1
            lst = [d1_amt, quarter_amt, dime_amt, nickel_amt, i]
            if (not p and i == 0) or (p):
                combs.append(lst)
        end = int(max_penny+1) - (d1_amt * 100)
        for x in range(0, end)[::-25]:
            if x != end-1 and x != max_penny:
                quarter_amt += 1
                lst = [d1_amt, quarter_amt, dime_amt, nickel_amt, x]
                if (not p and x == 0) or (p):
                    combs.append(lst)
            end = int(max_penny + 1) - (d1_amt * 100) - (quarter_amt * 25)
            for y in range(0, end)[::-10]:
                if y != end-1 and y != max_penny:
                    dime_amt += 1
                    lst = [d1_amt, quarter_amt, dime_amt, nickel_amt, y]
                    if (not p and y == 0) or (p):
                        combs.append(lst)
                end = int(max_penny + 1) - (d1_amt * 100) - (quarter_amt * 25) - (dime_amt * 10)
                for z in range(0, end)[::-5]:
                    if not n:
                        break
                    if z != max_penny and z != end-1:
                        nickel_amt += 1
                        lst = [d1_amt, quarter_amt, dime_amt, nickel_amt, z]
                        if (not p and z == 0) or (p):
                            combs.append(lst)
                nickel_amt = 0
                if not d:
                    break
            dime_amt = 0
            if not q:
                break
        quarter_amt = 0
        if not d1:
            break
    return combs



