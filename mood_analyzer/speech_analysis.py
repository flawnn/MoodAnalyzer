# coding=utf-8
import nltk
import re


def get_results(tweets):
    words = __WordAnalysis(tweets).fetchall()
    goodness_tester = __WordGoodness()
    dct = goodness_tester.parse_dict_file('german.lex')
    #dct = goodness_tester.parse_own_dict()
    return goodness_tester.word_meaning(words, dct)


class __WordGoodness:
    def parse_dict_file(self, fname):
        """
        Parses the dictionary file
        :param fname: (str) path to file
        :return: (tuple) ((int) good word count, (int) bad words count)
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

    def parse_own_dict(self):
        """
        Does the same as the function above, but with a own dictionary
        :return: (tuple) ((int) good word count, (int) bad words count)
        """

        words = {
            "toll": 1,
            "Liebe": 1,
            "gut": 1,
            "geil": 1,
            "cool": 1,
            "swag": 1,
            "krass": 1,
            "Hammer": 1,
            "Empathie": 1,
            "Dank": 1,
            "gediegen": 1,
            "Nice": 1,
            "schön": 1,
            "wundervoll": 1,
            "super": 1,
            "mega": 1,
            "Vorfreude": 1,
            "Freude": 1,
            "süß": 1,
            "lustig": 1,
            "nett": 1,
            "Erfolg": 1,
            "sozial": 1,
            "erfolgreich": 1,
            "Motivation": 1,
            "scheiße": 0,
            "asozial": 0,
            "Spast": 0,
            "Dummkopf": 0,
            "Mist": 0,
            "Müll": 0,
            "doof": 0,
            "schlecht": 0,
            "Ärger": 0,
            "ärgerlich": 0,
            "erschreckend": 0,
            "Krise": 0,
            "Ouh_shit": 0,
            "Katastrophe": 0,
            "verletzend": 0,
            "böse": 0,
            "krank": 0,
            "beleidigend": 0,
            "Trauer": 0,
            "schade": 0,
            "ungeheuerlich": 0,
            "Fehler": 0,
            "miserabel": 0,
            "abwertend": 0,
            "unhöflich": 0,
            "frech": 0
        }
        return words

    def word_meaning(self, frequently_words, word_dict):
        """
        Search meanings in the given words
        :param frequently_words: (list) [(tuple) ((str) word, (int) frequency), ...]
        :param word_dict: (dict) words with 1 for good and 0 for bad
        :return: (tuple) how many positive and negative words
        """

        pos, neg = 0, 0
        for Wort in frequently_words:
            if Wort[0] in word_dict:
                if word_dict[Wort[0]] < 0:
                    neg -= word_dict[Wort[0]] * Wort[1]

                if word_dict[Wort[0]] > 0:
                    pos += word_dict[Wort[0]] * Wort[1]

        return pos, neg


class __WordAnalysis:
    def __init__(self, to_analyze):
        """
        Constructor
        :param to_analyze: (list) [(str) tweet, ...]
        """

        self.__VALID_CHARS = "^[a-zA-ZÄÖÜäöüß]*$"
        self.__TO_ANALYZE = to_analyze

    def fetchall(self):
        """
        Fetches the most common words
        :return: (list) [(tuple) (word, count), ...]
        """

        string2 = self.Wortliste(self.__TO_ANALYZE)
        Anzahl = nltk.FreqDist(string2).most_common()
        wordcheck = [(x[0], x[1]) for x in Anzahl
                     if re.match(self.__VALID_CHARS, x[0]) is not None]
        return wordcheck

    def Wortliste(self, string):
        liste = []
        for tweet in string:
            liste = liste + re.split(r'[^a-zA-ZÄÖÜäöüß]+', tweet)

        return liste


if __name__ == '__main__':
    print(get_results(['#jugendhackt https://pic.twitter.com/NHIbtj4VKv',
'@jugendhackt @codeweekaward @WebDaysBerlin #cybercybercyber',
'Auf dem Weg nach Hause, Problem mist #schade holen ¯\_(ツ)_/¯ #jugendhackt',
'@Milletimisev @jugendhackt @Linuzifer Gnade buzzword Bingo wie die Großen &lt;3',
'@Milletimisev Ich Leider müssen heute viele traurige Alkpakas sterben würds kaufen.  :-) @jugendhackt @Linuzifer',
'OH: „Tinder für Geigerzähler - as a Service“ #jugendhackt',
'Jauchzjuhe: @codeweekaward, @jugendhackt & @WebDaysBerlin gleichzeitig dieses WE in Bln zum coden, hacken, #netzpolitik diskutieren #cyber',
'@jugendhackt Right back at ya!',
'Bei #jugendHackt suchen sie Daten zu Sportstätten. @katzenschiff hat welche aus Hamburg, ich aus #Moers 😅']))
    #print(__WordAnalysis(['Trump ist doof', 'Test test test ']).fetchall())