# # Basic Data Types
# Number(Integer, Floating), Sequence(String, List, Tuple)

# # # Number -> Integer ------------------------------------
#
production_cost = 2000
distribution_cost = 500
tax = 100.52342353
overall_sales = 5000
#
# print('Production Cost = ', production_cost)
# print('Production Cost Data Type = ', type(production_cost))

#
#
# # Number -> Floating -----------------------------------

# print('Tax = ', tax)
# print(int(tax))
# print('Tak Data Type = ', type(tax))

# Limiting floating point number
# print('Two decimal point = ', round(tax, 3))
# print('Two decimal point = ', "{:.3f}".format(tax))

# # # Sequence -> String ----------------------------------
first_name = "Rejaul Islam"
last_name = 'Royel'

# print('First Name = ', first_name)
# print(type(first_name))
# print('Last Name = ', last_name)
# print(type(last_name))
# #
# # Join String ---------------------------------------
full_name = first_name + last_name
# print('Full Name = ', full_name)

# String Concatenation
# full_name = first_name + ' ' + last_name
# print('Full Name = ', full_name)
# print('Full Name = ', first_name + ' ' + last_name)
#
# sales = 404034
# print(sales)
# print(type(sales))
#
# print('Your Sales is = ', sales, 'TK')

# # # Sequence -> List -------------------------------
# blank_list = []
# print(type(blank_list))

num_list = [1, 2, 35, 7, 4, 6, 4, 6, 64, 3, 2]
name_list = ['Sagir', 'Kanon', 'BM. Ashik', "Royel", 'Rabby']
multiple_data = [10, 20, 4, 'Twelve', 6, 'Orange']

# print(num_list)
#
# print(type(multiple_data))
# Index
num = num_list[2]
# print(num)

# # print(num_list)
# # print(name_list)
# #
# # print('Num_list type', type(num_list))
# # print('name_list type', type(name_list))

num_list = [1, 2, 35, 7, 4, 6, 4, 6, 64, 3, 2]
# # Sorting list elements
# print(num_list[0])
# print(num_list[0:4])
# print(num_list[:2])
# print(num_list[2:5])
#
# # # Arithmetic operation in list
# first = num_list[0]
# second = num_list[1]
# third = first + second
# print(third)
#
# # # Nested List -------------------------------------
nested_list = [['A', 'B'], [10, 20]]

# print(nested_list[0])
# print(nested_list[0][1])
# #
#
# # # ------------- List  Operations ------------------
#
# # Insert item in the list---------------------------
#
# print('Our Number list = ', num_list)
# num_list.append(30)
# print(num_list)
#
# # # Insert Item in specific location of the list --
# num_list.insert(2, 50)
# print('Adding 50 in 3rd position = ', num_list)
#
# # # Insert multiple elements in the list ----------
# num_list.extend([100, 200, 300])
# print(num_list)
#
#
# # # Removing item from list -----------------------
# print(num_list)
# # Remove by elements value
# num_list.remove(1)
# print(num_list)
#
# # # Remove by range
# List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print(list)
#
# for i in range(1, 6):
#     List.remove(i)
# print(List)
#
# # # Applying function in the list ---------------------
# print(num_list)
# print('Count Length = ', len(num_list))
# #
# # print('After Sorting Elements ')
# num_list.sort()
# print(num_list)
# #
# # print('Reverse Elements = ')
# num_list.reverse()
# print(num_list)
# #
# print('Sum list item = ', sum(num_list))
# #
# print('Max item = ', max(num_list))
# print('Min item = ', min(num_list))
#
#
# # # Sequence => Tuple---------------------------------
# # # Tuple is faster than list but you can not insert an element in the tuple

# tuple = ('This', 'is', 'a', 'Tuple')
# print('Tuple = ', tuple)
# print('Type is = ', type(tuple))
#
# print(tuple[0])
