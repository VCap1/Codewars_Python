from collections import Counter
def anagram(word, words):
    return [w for w in words if Counter(w) == Counter(word)]
