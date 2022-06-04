import pandas as pd

data = pd.read_html("https://en.wikipedia.org/wiki/List_of_massacres_in_Great_Britain")
data[0].to_csv("./UK.csv", index=False)
