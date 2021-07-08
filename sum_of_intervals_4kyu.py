def sum_of_intervals(intervals):
    return len(set([x for a, b in intervals for x in list(range(a,b))]))
