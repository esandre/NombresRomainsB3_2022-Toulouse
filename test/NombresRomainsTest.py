import unittest

import ConvertisseurNombresRomains


class MyTestCase(unittest.TestCase):
    def test_one(self):
        # ETANT DONNE le chiffre 1
        nombre = 1

        # QUAND on le convertit en nombres romains
        result = ConvertisseurNombresRomains.convertir(nombre)

        # ALORS on obtient 'I'
        self.assertEqual('I', result)

    def test_two(self):
        # ETANT DONNE le chiffre 2
        nombre = 2

        # QUAND on le convertit en nombres romains
        result = ConvertisseurNombresRomains.convertir(nombre)

        # ALORS on obtient 'II'
        self.assertEqual('II', result)

    def test_three(self):
        # ETANT DONNE le chiffre 3
        nombre = 3

        # QUAND on le convertit en nombres romains
        result = ConvertisseurNombresRomains.convertir(nombre)

        # ALORS on obtient 'III'
        self.assertEqual('III', result)

    def test_four(self):
        # ETANT DONNE le chiffre 4
        nombre = 4

        # QUAND on le convertit en nombres romains
        result = ConvertisseurNombresRomains.convertir(nombre)

        # ALORS on obtient 'IV'
        self.assertEqual('IV', result)

    def test_five(self):
        # ETANT DONNE le chiffre 5
        nombre = 5

        # QUAND on le convertit en nombres romains
        result = ConvertisseurNombresRomains.convertir(nombre)

        # ALORS on obtient 'V'
        self.assertEqual('V', result)


if __name__ == '__main__':
    unittest.main()
