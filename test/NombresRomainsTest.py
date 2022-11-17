import unittest
import parameterized as parameterized
import ConvertisseurNombresRomains


class MyTestCase(unittest.TestCase):

    @parameterized.parameterized.expand([[1], [2], [3]])
    def test_unité(self, n):
        # ETANT DONNE un chiffre <n> entre 1 et 3
        # QUAND on le convertit en nombres romains
        result = ConvertisseurNombresRomains.convertir(n)

        # ALORS on obtient <n> fois 'I'
        attendu = 'I'*n
        self.assertEqual(attendu, result)

    @parameterized.parameterized.expand([[5], [6], [7], [8]])
    def test_cinq_plus_unité(self, n):
        # ETANT DONNE un chiffre <n> entre 5 et 8
        # QUAND on le convertit en nombres romains
        result = ConvertisseurNombresRomains.convertir(n)

        # ALORS on obtient 'V' plus <n-5> fois 'I'
        attendu = 'V' + 'I' * (n - 5)
        self.assertEqual(attendu, result)

    def test_quatre(self):
        # ETANT DONNE le chiffre 4
        nombre = 4

        # QUAND on le convertit en nombres romains
        result = ConvertisseurNombresRomains.convertir(nombre)

        # ALORS on obtient 'IV'
        self.assertEqual('IV', result)

    def test_neuf(self):
        # ETANT DONNE le chiffre 9
        nombre = 9

        # QUAND on le convertit en nombres romains
        result = ConvertisseurNombresRomains.convertir(nombre)

        # ALORS on obtient 'IX'
        self.assertEqual('IX', result)

    def test_quatorze(self):
        # ETANT DONNE le chiffre 14
        nombre = 14

        # QUAND on le convertit en nombres romains
        result = ConvertisseurNombresRomains.convertir(nombre)

        # ALORS on obtient 'XIV'
        self.assertEqual('XIV', result)

    def test_quinze(self):
        # ETANT DONNE le chiffre 15
        nombre = 15

        # QUAND on le convertit en nombres romains
        result = ConvertisseurNombresRomains.convertir(nombre)

        # ALORS on obtient 'XV'
        self.assertEqual('XV', result)

    @parameterized.parameterized.expand([[10], [11], [12], [13]])
    def test_dix_plus_unité(self, n):
        # ETANT DONNE un chiffre <n> entre 10 et 13
        # QUAND on le convertit en nombres romains
        result = ConvertisseurNombresRomains.convertir(n)

        # ALORS on obtient 'X' plus <n-10> fois 'I'
        attendu = 'X' + 'I' * (n - 10)
        self.assertEqual(attendu, result)


if __name__ == '__main__':
    unittest.main()
