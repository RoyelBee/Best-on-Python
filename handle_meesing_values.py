# # ---------------- Working with missing values ---------------
# # ------------------------------------------------------------
import pandas as pd

# To convert in int to float
df = pd.DataFrame()
df.columnName.astype('float64')

# # Find total number of missing values
totalMissing = df.columnName.isnull().sum()

# # Replace one value with another values
# # Replace A with B
df.columnName.replace("A", "A")
