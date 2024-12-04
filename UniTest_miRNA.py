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
            validExtract.write("64685 MI0000001 cel-let-7 cel-let-7L Caenorhabditis elegans let-7 stem-loop UACAC let-7 is found on chromosome X in Caenorhabditis elegans [1] and pairs to sites within the 3' untranslated region (UTR) of target mRNAs, specifying the translational repression of these mRNAs and triggering the transition to late-larval and adult stages [2]. 58 0\n")
            validExtract.write("64790 MI0000114 hsa-mir-107 hsa-mir-107-10 Homo sapiens miR-107 stem-loop CUCUC This miRNA was identified by homology to miR-103 [1], and later verified by cloning in human [2]. 22 0\n")
            validExtract.write("64795 MI0000119 dme-mir-2b-1 Drosophila melanogaster miR-2b-1 stem-loop CUUCA Stark et al. [2] have identified targets for miR-2 in Drosophila using computational prediction followed by experimental validation. miR-2 regulates the proapoptotic genes reaper, grim and sickle, suggesting that it may be involved in the control of apoptosis. 44 0")

        self.target_species = ["Caenorhabditis elegans", "Homo sapiens", "Drosophila melanogaster"]

    def test_extract_miRNAValid(self):
        resultat = extract_miRNA(self.valid_extract, self.target_species)
        print("Résultat extrait:", resultat)
        attendu = {"Caenorhabditis elegans": ["UACAC"], "Homo sapiens": ["CUCUC"], "Drosophila melanogaster": ["CUUCA"]}
        self.assertEqual(resultat, attendu)


    
    def tearDown(self):
        os.remove("valid_miRNA.txt")






if __name__ == "__main__":
    unittest.main()
