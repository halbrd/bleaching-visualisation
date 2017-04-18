import pandas as pd
import json

# Read Excel spreadsheet into DataFrame
df = pd.read_excel("data.xlsx", sheetname="Sites - BDVA")
# Convert site_index to string
df["site_index"] = df["site_index"].astype(str)
# Set site_index as row index
df = df.set_index("site_index", drop=False)
# Condense multiple spaces in reef_name
df["reef_name"] = df["reef_name"].str.replace(" +", " ")
# Standardize null values to None
df = df.where(pd.notnull(df), None)

# Export to JSON
json.dump(df.to_dict(orient="index"), open("data.json", "w"), indent="\t")
# Export to CSV
df.to_csv(path_or_buf="data.csv", index=False)
