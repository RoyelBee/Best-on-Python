import pandas as pd
import pyodbc as db

# # Create Database connection---------------------------------
# connection = db.connect('DRIVER={SQL Server};'
#                         'SERVER=137.116.139.217;'
#                         'DATABASE=ARCHIVESKF;'
#                         'UID=sa;PWD=erp@123')
#
#
# query = """ select top 1000 * from OEsalesDetails """
#
# data = pd.read_sql_query(query, connection)
# data.to_csv('sales_data.csv', index=False)
# print('Data Saved')

# print(type(data))

# # Get data from csv files ----------------------------------
data = pd.read_csv('D:/Python Code/Best-on-Python/sales_data.csv')

# print(data.head(4))
# print(type(data))


# # Creating DataFrame ----------------------------------------
# df = pd.DataFrame({'Yes': [10, 20], 'No': [4, 30]})
# print(df)

# df1 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
#                     'Sue': ['Pretty good.', 'Bland.']})
# print(df1)

# Set Index
# df2 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
#                     'Sue': ['Pretty good.', 'Bland.']},
#                    index=['0', '1'])
# print(df2)


# # Working with dataset ---------------------------------------
# # Print all columns
# print(data.columns)

# # Print Dataset shape
# print(data.shape)

# Select fixed columns
# print(data.AUDTORG)
# print(data.AUDTORG.tolist())

# print(data['AUDTORG'])

# Select Multiple columns
# print(data.loc[:, ['AUDTORG',  'TRANSDATE', 'EXTINVMISC']])

# Select by rows ( First rows or budget column)
# print(data.AUDTORG.iloc[0])

# Select fixed column and row
# print(data.AUDTORG[100])

# Select by index  [:1] indicates total number of rows with all columns
# print(data.iloc[:2])

# # Condition
rng = data.loc[(data.AUDTORG == 'RNGSKF')]
print(rng)


# # To Write csv Files
# # data.to_csv('DataName.cv')
