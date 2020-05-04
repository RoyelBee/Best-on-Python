import pandas as pd
#
# # Creating DataFrame
# # df = pd.DataFrame({'Yes': [10, 20], 'No': [4, 30]})
# # print(df)
# #
# # df1 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
# #                     'Sue': ['Pretty good.', 'Bland.']})
# # print(df1)
#
# # #Set Index
# # df2 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
# #                     'Sue': ['Pretty good.', 'Bland.']},
# #                    index = ['Index1', 'Index2'])
# # print(df2)
#
# # # Creating Series
# # series = pd.Series([1, 2, 3, 4, 5])
# # print(series)
#
# series = pd.Series([10, 20, 30, 40, 50],
#                    index= ['User 1', 'User 2', 'User 3', 'User 4', 'User 5'],
#                    name='Product A')
# # # Series does not have any column name its only have name
# # print(series)
#
#
# # # Read DataFrame
# movie_data = pd.read_csv('Data/movie_metadata.csv', index_col=0)
# # print(movie_data.head())
#
# # # Select specefic columns
# # print(movie_data.director_name)
#
# # # Get Data by location
# # print(movie_data.iloc[0])
# print(movie_data.movie_title[:10])
#
#
# # Read all columns
# print(movie_data.columns)
#
#
# # # To Write csv Files
# # data.to_csv('DataName.cv')



