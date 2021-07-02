  '''
  a basic implementation of Kadane's Algorithm
  '''
def max_sequence(arr):
    if len(arr) > 0:
        max_sum = cur_sum = 0
        for el in arr:
            cur_sum = max(el + cur_sum, el)
            max_sum = max(cur_sum, max_sum)

        return max_sum
    return 0
