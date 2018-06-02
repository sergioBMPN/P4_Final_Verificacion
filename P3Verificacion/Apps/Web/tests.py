from django.test import TestCase
from .strings_example import StringsExamples

class TestStringsExamples(TestCase):
    def test_normal_text(self):
        string = "hola me llamo juan"
        result = StringsExamples.count_words(string)
        assert StringsExamples.cmp(result,[('juan', 1), ('llamo', 1), ('hola', 1)])

    def test_upper_text(self):
        string = "HOLA ME LLAMO JUAN"
        result = StringsExamples.count_words(string)
        assert StringsExamples.cmp(result,[('juan', 1), ('llamo', 1), ('hola', 1)])

    def test_upper_with_lower_text(self):
        string = "HoLa Me LlAmo JuaN"
        result = StringsExamples.count_words(string)
        assert StringsExamples.cmp(result,[('juan', 1), ('llamo', 1), ('hola', 1)])

    def test_count_words_in_normal_text(self):
        string = "hola me llamo juan hola"
        result = StringsExamples.count_words(string)
        assert StringsExamples.cmp(result,[('hola', 2), ('juan', 1), ('llamo', 1)])

    def test_count_words_in_upper_text(self):
        string = "HoLa hOlA mE LlaMo JuAn"
        result = StringsExamples.count_words(string)
        assert StringsExamples.cmp(result,[('hola', 2), ('juan', 1), ('llamo', 1)])

    def test_count_words_without_art(self):
        string = "El perro perro de mi primo es de color marron"
        result = StringsExamples.count_words(string)
        assert StringsExamples.cmp(result,[('perro', 2), ('marron', 1), ('color', 1), ('es', 1), ('primo', 1)])

    def test_count_words_without_prep(self):
        string = "El coche coche se dirige hacia el colegio"
        result = StringsExamples.count_words(string)
        assert StringsExamples.cmp(result,[('coche', 2), ('colegio', 1), ('dirige', 1)])

    def test_count_words_without_pron(self):
        string = "Aquellos chicos juegan al futbol, mientras que esos chicos a las canicas"
        result = StringsExamples.count_words(string)
        assert StringsExamples.cmp(result,[('chicos', 2), ('canicas', 1), ('mientras', 1), ('futbol', 1), ('juegan', 1)])

    def test_count_words_without_punt(self):
        string = "Los chicos de mi clase estudian ingles, los chicos de segundo frances, y los chicos de tercero italiano."
        result = StringsExamples.count_words(string)
        assert StringsExamples.cmp(result,[('chicos', 3), ('italiano', 1), ('tercero', 1), ('frances', 1), ('segundo', 1), ('ingles', 1), ('estudian', 1), ('clase', 1)])

    def test_count_words_start_with_space(self):
        string = " La prueba de que el texto empiece por un espacio espacio"
        result = StringsExamples.count_words(string)
        assert StringsExamples.cmp(result,[('espacio', 2), ('empiece', 1), ('texto', 1), ('prueba', 1)])

    def test_count_words_end_with_space(self):
        string = "La prueba de que el texto termine por un espacio espacio "
        result = StringsExamples.count_words(string)
        assert StringsExamples.cmp(result,[('espacio', 2), ('termine', 1), ('texto', 1), ('prueba', 1)])

    def test_count_words_more_than_one_space(self):
        string = "La prueba    de         que  el    texto    tenga  mas de un           espacio                espacio"
        result = StringsExamples.count_words(string)
        assert StringsExamples.cmp(result,[('espacio', 2), ('tenga', 1), ('texto', 1), ('prueba', 1)])

    def test_count_words_with_rare_caracters(self):
        string = "El * texto tiene carateres raros"
        result = StringsExamples.count_words(string)
        assert StringsExamples.cmp(result,[('raros', 1), ('carateres', 1), ('tiene', 1), ('texto', 1)])

    def test_count_words_with_rare_caracters_two(self):
        string = "  EL texto    (TiEnE .carateres    raROS  "
        result = StringsExamples.count_words(string)
        assert StringsExamples.cmp(result,[('raros', 1), ('carateres', 1), ('tiene', 1), ('texto', 1)])

    def test_no_countain(self):
        string=""
        result = StringsExamples.count_words(string)
        assert result == []

    def test_only_stopwords(self):
        string = "pero"
        result = StringsExamples.count_words(string)
        print(result)
        assert result == []