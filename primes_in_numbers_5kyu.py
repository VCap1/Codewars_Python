from collections import Counter
def prime_factors(n: int = 7775460):
    sol, i = Counter(), 2
    while n/i != 1:
        if n % i == 0: 
            sol.update([i])
            n = n/i
        else:
            i += 1
    sol.update([i])
    
    return "".join([f'({el}**{val})' if val > 1 else f'({el})' for el, val in sol.items()])
