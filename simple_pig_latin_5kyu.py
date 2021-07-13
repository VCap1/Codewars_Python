import string 
def pig_it(text):
    return " ".join( [t[1:] + t[:1] + 'ay' if t not in list(string.punctuation) else t for t in text.split(" ")  ])
