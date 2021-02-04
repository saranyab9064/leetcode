def helper(n):
    res = 0
    for i in range(0, len(n)):
        res = res + int(n[i]) * int(n[i])
    return str(res)


def sum_val(n):

    temp = helper(str(n))
    print(temp)
    fin_val = 0
    while temp:
        if len(temp)>1:
            out = helper(temp)
            temp = out
        else:
            print(temp)
            fin_val = temp
            temp = False
    if int(fin_val) != 1:
        return False
    else:
        return True


a = 64
print(sum_val(a))


