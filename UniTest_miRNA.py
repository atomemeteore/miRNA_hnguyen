#
#-*- encoding : utf-8 -*-

from project_miRNA import read_species
import unittest
import os

class TestUnitaire(unittest.TestCase):

    def setUp(self):

        self.valid_file = "valid_species.txt"
        with open(self.valid_file, "w") as valid:
            valid.write("Mus musculus\n")
            valid.write("Drosophila melanogaster\n")
            valid.write("Homo sapiens")

        self.empty_file = "empty_file.txt"
        with open(self.empty_file, "w", encoding="utf-8"):
            pass

        self.incorrect_file = "incorrect_file.txt"
        with open(self.incorrect_file, "w") as incorrect:
            incorrect.write("Mus musculus\n")
            incorrect.write("55569\n")
            incorrect.write("-------\n")
            incorrect.write("Homo sapiens")

    def test_readSpeciesValid(self):
        resultat = read_species(self.valid_file)
        attendu = ["Mus musculus", "Drosophila melanogaster", "Homo sapiens"]
        self.assertEqual(resultat,attendu)

    def test_readSpeciesEmpty(self):
        resultat = read_species(self.empty_file)
        attendu = []
        self.assertEqual(resultat,attendu)

    def test_readSpeciesIncorrect(self):
        resultat = read_species(self.incorrect_file)
        attendu = ["Mus musculus", "Homo sapiens"]


    def tearDown(self):
        os.remove(self.valid_file)
        os.remove(self.empty_file)
        os.remove(self.incorrect_file)


if __name__ == "__main__":
    unittest.main()