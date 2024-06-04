import pandas as pd

df = pd.read_csv("test.csv")

df.to_html("ourdf.html")