#
#-*- encoding : utf-8 -*-

from project_miRNA import read_species, extract_miRNA
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
        self.assertEqual(resultat,attendu)

    def tearDown(self):
        os.remove(self.valid_file)
        os.remove(self.empty_file)
        os.remove(self.incorrect_file)


class TestMiRNAExtraction(unittest.TestCase):
    def setUp(self):
        self.valid_extract = "valid_miRNA.txt"
        with open(self.valid_extract, "w") as validExtract:
            validExtract.write("64690 MI0000006 cel-mir-35 Caenorhabditis elegans miR-35 stem-loop UCUCGGAUCAGAUCGAGCCAUUGCUGGUUUCUUCCACAGUGGUACUUUCCAUUAGAACUAUCACCGGGUGGAAACUAGCAGUGGCUCGAUCUUUUCC 58 0\n")
            validExtract.write("64818 MI0000142 mmu-mir-27b Mus musculus miR-27b stem-loop AGGUGCAGAGCUUAGCUGAUUGGUGAACAGUGAUUGGUUUCCGCUUUGUUCACAGUGGCUAAGUUCUGCACCU 30 0\n")
            validExtract.write("64808 MI0000132 dme-mir-12 Drosophila melanogaster miR-12 stem-loop UACGGUUGAGUAUUACAUCAGGUACUGGUGUGCCUUAAAUCCAACAACCAGUACUUAUGUCAUACUACGCCGUG 44 0\n")

        self.target_species = ["Caenorhabditis elegans", "Homo sapiens", "Drosophila melanogaster"]

    def test_extract_miRNAValid(self):
        f = self.valid_extract
        resultat = extract_miRNA(f, self.target_species)
        attendu = {"Caenorhabditis elegans": ["UCUCGGAUCAGAUCGAGCCAUUGCUGGUUUCUUCCACAGUGGUACUUUCCAUUAGAACUAUCACCGGGUGGAAACUAGCAGUGGCUCGAUCUUUUCC"], "Mus musculus": ["AGGUGCAGAGCUUAGCUGAUUGGUGAACAGUGAUUGGUUUCCGCUUUGUUCACAGUGGCUAAGUUCUGCACCU"], "Drosophila melanogaster": ["UACGGUUGAGUAUUACAUCAGGUACUGGUGUGCCUUAAAUCCAACAACCAGUACUUAUGUCAUACUACGCCGUG"]}
        self.assertEqual(resultat, attendu)
    
    def tearDown(self):
        os.remove("valid_miRNA.txt")






if __name__ == "__main__":
    unittest.main()
