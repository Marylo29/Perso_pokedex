import pandas as pd

"""Module of the core version of pokedex."""

pokedex_en = pd.read_csv("sources/Pokemon_en.csv",sep = ',')
type_table_csv = pd.read_csv("sources/type_table.csv",sep = ';')


def make_list_type_table(data:pd.DataFrame) -> list[dict]:
    """
    Convert a .csv table type file into a list of dict

    Args:
        data (pd.DataFrame): a pandas dataframe

    Returns:
        list[dict]: list of number of types dictionnary 
    """
    type_table = []
    for i in range(len(data)):
        line = data.iloc[i]
        new = {'Type':line.iloc[0],'Resistance':[],'Faiblesse':[],'Immunité':[]}
        for type_a,texte in line.items():
            if texte == '2':
                new['Faiblesse'].append(type_a)
            elif texte == '½':
                new['Resistance'].append(type_a)
            elif texte == '0':
                new['Immunité'].append(type_a)
        type_table.append(new.copy())
    return type_table

types_en = ['Grass', 'Fire', 'Water', 'Bug', 'Normal', 'Poison', 'Electric', 'Ground', 'Fairy', 'Fighting', 'Psychic', 'Rock', 'Ghost', 'Ice', 'Dragon', 'Dark', 'Steel', 'Flying']
types_table_fr = make_list_type_table(type_table_csv)


class Pokemon:
    def __init__(self,name:str,types:tuple):
        """
        Create a pokemon object

        Args:
            name (str): the name of the pokemon
            types (tuple): tuple of the types of the pokemon 
        """
        self.name = name
        self.types = types