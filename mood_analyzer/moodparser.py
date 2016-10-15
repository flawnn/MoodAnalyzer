
def parse_dict_file(fname):
    """
    Parses the dictionary file
    :param fname: (str) path to file
    :return:  (dict) {(str) word: (int) 1/-1} (1 is good, -1 is bad)
    """

    result = {}
    with open(fname) as f:
        for line in f.readlines():
            if not line.startswith('%%'):
                words = line.split()
                sign, value = words[1].split('=')
                if sign == "POS":
                    result[words[0]] = +1

                elif sign == "NEG":
                    result[words[0]] = -1

    return result



