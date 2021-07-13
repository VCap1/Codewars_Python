def pig_it(text):
    return " ".join( [t[1:] + t[:1] + 'ay' for t in text.split(" ")])
