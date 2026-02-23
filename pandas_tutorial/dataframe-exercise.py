import pandas as pd

footballers = {"Name" : ["Ancelotti" , "Ronaldo", "De Bruyne", "Cortouis"],
               "Role" : ["Coach", "Striker", "Midfielder", "Goalkeeper"],
               "Country" : ["Italy", "Portugal", "Belgium", "Belgium"]}

df = pd.DataFrame(footballers, index=["1.", "2.", "3.", "4."])

df["Hair"] = ["Classy", "Cool", "Blonde", "Short"]

new_guy = pd.DataFrame([{"Name" : "Messi", "Role" : "Forward", "Country" : "Argetina"}])
df = pd.concat([df, new_guy])

print(df)