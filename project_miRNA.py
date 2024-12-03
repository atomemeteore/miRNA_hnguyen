#
# -*- coding : utf-8 -*-

"""
Sur le site de Mirbase (https://www.mirbase.org/) consacré aux micro-arn on peut
trouver, pour chaque version, un fichier nommé mirna.txt dont voici les premières lignes
de la version courante :

64685 MI0000001 cel-let-7 cel-let-7L Caenorhabditis elegans let-7 stem-loop UACACUGUGGAUCCGGUGAGGUAG
64686 MI0000002 cel-lin-4 cel-lin-4L Caenorhabditis elegans lin-4 stem-loop AUGCUUCCGGCCUGUUCCCUGAGA
64687 MI0000003 cel-mir-1 Caenorhabditis elegans miR-1 stem-loop AAAGUGACCGUACCGAGCUGCAUACUUCCUUACAU
64688 MI0000004 cel-mir-2 Caenorhabditis elegans miR-2 stem-loop UAAACAGUAUACAGAAAGCCAUCAAAGCGGUGGUU
64689 MI0000005 cel-mir-34 Caenorhabditis elegans miR-34 stem-loop CGGACAAUGCUCGAGAGGCAGUGUGGUUAGCUG
64690 MI0000006 cel-mir-35 Caenorhabditis elegans miR-35 stem-loop UCUCGGAUCAGAUCGAGCCAUUGCUGGUUUCUU

Le travail demandé consiste à écrire un programme Python qui lit des noms d’espèces
dans un fichier nommé species.txt (un nom d’espèce par ligne) et qui ensuite lit un
fichier structuré comme le fichier mirna.txt ci-dessus ligne par ligne et qui calcule pour
chaque espèce présente dans le fichier species.txt le pourcentage de chacun des quatre
acides nucléiques (A, C, G, U) et qui affiche les résultats sous la forme de camemberts (un
par espèce et un pour toutes les espèces contenues dans le fichier species.txt).
Vous devez déposer une archive compressée contenant votre programme sur Universitice pour le 20 décembre 2024.
"""

import re

species_file = "species.txt"
miRNA_file = "mirna.txt"

def read_species(species_file):
    liste_species = []
    pattern_specie = re.compile(r"^[A-Z][a-z]+ [a-z]+$")
    with open(species_file,"r") as fichier :
        for ligne in fichier :
            if re.match(pattern_specie,ligne):
                liste_species.append(ligne.strip())
            else :
                pass
        return liste_species
    
print(read_species(species_file))

target_species = read_species(species_file)

def extract_miRNA(fichier,target_species):
    species_sequences =  {specie: [] for specie in target_species}
    pattern = re.compile(r"(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+([A-Za-z]+\s+[a-z]+)\s+.*stem-loop\s+([ACGU]+)")
    with open("mirna.txt","r") as fichier:
        for line in fichier:
            match = pattern.match(line)
            if match:
                specie = match.group(5)
                sequence = match.group(6)
                if specie in target_species:
                    species_sequences[specie].append(sequence)
    return species_sequences

