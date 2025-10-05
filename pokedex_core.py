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
    def __init__(self,identifiant:int,name:str,form:str,types:tuple,stats:tuple,gen:int):
        """
        Créer un Pokémon

        Args:
            identifiant (int): Identifiant du pokédex
            name (str): _description_
            form (str): _description_
            types (tuple): _description_
            stats (tuple): _description_
            gen (int): _description_
        """
        self._id = identifiant
        self._name = name
        self._surname = None
        self._form = form
        self._types = types
        self._stats = stats
        self._gen = gen

    @property
    def surnom(self):
        return self._surname
    
    @surnom.setter
    def surnom(self,surnom):
        self._surname = surnom
    
    @property
    def id(self):
        return self._id
    
    @property
    def nom(self):
        return self._name
    
    @property
    def types(self):
        return self._types
    
    @property
    def stats(self):
        return self._stats
    
    @property
    def stat_hp(self):
        self._stats[1]

    @property
    def stat_atk(self):
        self._stats[2]
    
    @property
    def stat_def(self):
        self._stats[3]

    @property
    def stat_sp_atk(self):
        self._stats[4]

    @property
    def stat_sp_def(self):
        self._stats[5]

    @property
    def stat_vit(self):
        self._stats[6]

    @property
    def gen(self):
        return self._gen
    
    @property
    def forme(self):
        return self._form
    
    def __str__(self):
        return f"ID : {self.id}, Nom : {self.nom}, Surnom : {self.surnom}, Forme : {self.forme}, Types : {self.types}, Stats : {self.stats}, Genération : {self.gen}"

if __name__ == "__main__":
    pokedex_liste = []
    for pokemon_spe in pokedex_en.itertuples():
        pokedex_liste.append(Pokemon(pokemon_spe[1],pokemon_spe[2],pokemon_spe[3],tuple(pokemon_spe[4:6]),tuple(pokemon_spe[6:13]),pokemon_spe[13]))
    for pokemon in pokedex_liste:
        print(pokemon)