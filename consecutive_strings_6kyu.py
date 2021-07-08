def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ""
    cur_len = 0 
    res = ''
    for i,x in enumerate(strarr):
        cur = "".join(strarr[i:i+k])
        if len(cur) > cur_len:
            cur_len, res = len(cur), cur
    return res
