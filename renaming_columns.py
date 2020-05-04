import pandas as pd
df = pd.DataFrame()

# # Change column name A to B
df.rename(columns={'A': 'B'})
# # Or
renamed = df.rename(columns=dict(region_1='region', region_2='locale'))


# # Change Index Name ( It will set 0 index means first rows = 0-> firstEntry and second row = 1-> secondEntry
df.rename(index={0: 'firstEntry', 1: 'secondEntry'})
# # Or
df.rename_axis('wines', axis='rows')

# # Combining two dataframe
df3 = pd.concat([df1, df2])
