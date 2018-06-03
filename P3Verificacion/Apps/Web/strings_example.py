import collections


class StringsExamples(object):
    """A class to play with the strings"""

    @staticmethod
    def count_words(args):
        if args is None:
            resultado = []
        elif len(args) == 0:
            resultado = []
        else:
            vocales = ["a", "e", "i", "o", "u"]

            articulos = ["el", "la", "los", "las", "lo", "un", "uno", "una", "unos", "unas"]

            preposiciones = ['pero', 'hacia', 'del', 'incluso', 'mas', 'menos', 'y', 'a', 'ante', 'bajo', 'cabe', 'con',
                             'contra', 'de', 'desde', 'durante', 'en', 'entre', 'hasta', 'mediante', 'para', 'por',
                             'segun',
                             'sin', 'so', 'sobre', 'tras', 'versus', 'via', 'excepto', 'salvo', 'ademas', 'cual',
                             'cuales']

            pronombres = ['este', 'esta', 'esto', 'estos', 'estas', 'ese', 'esa', 'eso', 'esos', 'esas', 'aquel',
                          'aquella',
                          'aquellos', 'aquellas', 'le', 'les', 'yo', 'me', 'mi', 'conmigo', 'tu', 'te', 'ti', 'contigo',
                          'usted', 'vos', 'el', 'se', 'si', 'consigo', 'ella', 'ello', 'nosotros', 'nos', 'nosotras',
                          'vosotros', 'vosotras', 'os']

            puntuaciones = [",", ".", ";", ":", "-", "'", "*", "!", "?", "¡", "¿", "<", ">", "[", "]", "{", "}", "(", ")", '"',
                            "#", "%", "$", "="]

            otros = ["que", "de", "al", "su", "sus", " "]

            listaStopwords = []

            listaStopwords.extend(vocales)
            listaStopwords.extend(articulos)
            listaStopwords.extend(preposiciones)
            listaStopwords.extend(pronombres)
            listaStopwords.extend(otros)

            for punt in puntuaciones:
                args = args.replace(punt, "")
            args = args.lower()
            args = args.split()

            for stopwords in listaStopwords:
                try:
                    for palabra in args:
                        args.remove(stopwords)
                except AttributeError:
                    pass
                except ValueError:
                    pass

            counter = collections.Counter(args)

            resultado = counter.most_common()

        return resultado

    @staticmethod
    def cmp(a, b):
        for element in a:
            if element not in b:
                return False
        return True
