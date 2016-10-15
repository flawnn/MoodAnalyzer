
def read_moodlist(fname):
    result = {}
    with open(fname) as f:
        for line in f.readlines():
            if not line.startswith("%%"):
                word, value = line.split(" ")
                sign, value = value.split("=")
                value = float(value)
                if sign == "POS":
                    result[word] = +1
                if sign == "NEG":
                    result[word] = -1
    return result





