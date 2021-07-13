def pig_it(text):
    return " ".join( [t[1:] + t[:1] + 'ay' if t.isalpha() else t for t in text.split(" ")  ])
