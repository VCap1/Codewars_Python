from collections import Counter
def duplicate_count(text):
    c = Counter(text.lower())
    counter = len([x for x in c if c[x] > 1])
    return counter


'''
not my solution, but my personal favorite by codewars user WOnder93

return sum(1 for c, n in Counter(text.lower()).iteritems() if n > 1)
'''
