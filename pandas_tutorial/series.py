import pandas as pd

pokemons = ["Balbasaur", "Ivysaur", "Venesaur", "Charmander", "Charmeleon", "Charizard"]

series = pd.Series(pokemons, index=range(1,7))

print(series)