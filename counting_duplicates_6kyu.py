from collections import Counter
def duplicate_count(text):
    c = Counter(text.lower())
    counter = len([x for x in c if c[x] > 1])
    return counter
