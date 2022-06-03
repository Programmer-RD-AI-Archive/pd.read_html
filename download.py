import pandas as pd

data = pd.read_html("https://en.wikipedia.org/wiki/List_of_massacres_in_the_United_States")
data[0].to_csv("./data.csv", index=False)
