def dig_pow(n, p):
     t = sum([int(str(n)[i]) ** (p + i) for i in range(len(str(n)))])
     return t / n if (t % n) == 0 else -1
