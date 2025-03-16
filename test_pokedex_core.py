from pokedex_core import *
import unittest
import pandas as pd

class TestPokedexCore(unittest.TestCase):

    def test_make_list_type_table(self):
        """
        tests for the make_list_type_table function
        """
        type_table_csv = pd.read_csv("sources/type_table.csv",sep = ';')
        result = make_list_type_table(type_table_csv)

        expected = [
            {'Type': 'ACIER', 'Resistance': ['ACIER', 'DRAGON', 'FÉE', 'GLACE', 'INSECTE', 'NORMAL', 'PLANTE', 'PSY', 'ROCHE', 'VOL'], 'Faiblesse': ['COMBAT', 'FEU', 'SOL'], 'Immunité': ['POISON']},
            {'Type': 'COMBAT', 'Resistance': ['INSECTE', 'ROCHE', 'TÉNÈBRES'], 'Faiblesse': ['FÉE', 'PSY', 'VOL'], 'Immunité': []}, 
            {'Type': 'DRAGON', 'Resistance': ['EAU', 'ÉLECTRIK', 'FEU', 'PLANTE'], 'Faiblesse': ['DRAGON', 'FÉE', 'GLACE'], 'Immunité': []}, 
            {'Type': 'EAU', 'Resistance': ['ACIER', 'EAU', 'FEU', 'GLACE'], 'Faiblesse': ['ÉLECTRIK', 'PLANTE'], 'Immunité': []}, 
            {'Type': 'ÉLECTRIK', 'Resistance': ['ACIER', 'ÉLECTRIK', 'VOL'], 'Faiblesse': ['SOL'], 'Immunité': []}, 
            {'Type': 'FÉE', 'Resistance': ['COMBAT', 'INSECTE', 'TÉNÈBRES'], 'Faiblesse': ['ACIER', 'POISON'], 'Immunité': ['DRAGON']}, 
            {'Type': 'FEU', 'Resistance': ['ACIER', 'FÉE', 'FEU', 'GLACE', 'INSECTE', 'PLANTE'], 'Faiblesse': ['EAU', 'ROCHE', 'SOL'], 'Immunité': []}, 
            {'Type': 'GLACE', 'Resistance': ['GLACE'], 'Faiblesse': ['ACIER', 'COMBAT', 'FEU', 'ROCHE'], 'Immunité': []}, 
            {'Type': 'INSECTE', 'Resistance': ['COMBAT', 'PLANTE', 'SOL'], 'Faiblesse': ['FEU', 'ROCHE', 'VOL'], 'Immunité': []}, 
            {'Type': 'NORMAL', 'Resistance': [], 'Faiblesse': ['COMBAT'], 'Immunité': ['SPECTRE']}, 
            {'Type': 'PLANTE', 'Resistance': ['EAU', 'ÉLECTRIK', 'PLANTE', 'SOL'], 'Faiblesse': ['FEU', 'GLACE', 'INSECTE', 'POISON', 'VOL'], 'Immunité': []}, 
            {'Type': 'POISON', 'Resistance': ['COMBAT', 'FÉE', 'INSECTE', 'PLANTE', 'POISON'], 'Faiblesse': ['PSY', 'SOL'], 'Immunité': []}, 
            {'Type': 'PSY', 'Resistance': ['COMBAT', 'PSY'], 'Faiblesse': ['INSECTE', 'SPECTRE', 'TÉNÈBRES'], 'Immunité': []}, 
            {'Type': 'ROCHE', 'Resistance': ['FEU', 'NORMAL', 'POISON', 'VOL'], 'Faiblesse': ['ACIER', 'COMBAT', 'EAU', 'PLANTE', 'SOL'], 'Immunité': []}, 
            {'Type': 'SOL', 'Resistance': ['POISON', 'ROCHE'], 'Faiblesse': ['EAU', 'GLACE', 'PLANTE'], 'Immunité': ['ÉLECTRIK']}, 
            {'Type': 'SPECTRE', 'Resistance': ['INSECTE', 'POISON'], 'Faiblesse': ['SPECTRE', 'TÉNÈBRES'], 'Immunité': ['COMBAT', 'NORMAL']}, 
            {'Type': 'TÉNÈBRES', 'Resistance': ['SPECTRE', 'TÉNÈBRES'], 'Faiblesse': ['COMBAT', 'FÉE', 'INSECTE'], 'Immunité': ['PSY']}, 
            {'Type': 'VOL', 'Resistance': ['COMBAT', 'INSECTE', 'PLANTE'], 'Faiblesse': ['ÉLECTRIK', 'GLACE', 'ROCHE'], 'Immunité': ['SOL']}]

        self.assertEqual(result, expected, f"Le résultat de make_list_type_table() aurait du être {expected} mais vaut {result}.")



if __name__ == "__main__":
    unittest.main()