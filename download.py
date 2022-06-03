import pandas as pd

data = pd.read_html("https://en.wikipedia.org/wiki/List_of_best-selling_music_artists")
n_data = data[0]
for d_iter in data[1:]:
    n_data = n_data.append(d_iter)
print(n_data)
n_data.to_csv("./data.csv", index=False)
