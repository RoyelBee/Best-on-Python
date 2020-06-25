# # Basic Example -----------------------------------------------------
# # number1 = 10
# # number2 = 10
# #
# # if number1 <= number2:
# #     print('A')
# #
# # else:
# #     print('B')
#
#
# # # Example 2--------------------------------------------------------
# # name = 'Konon'
# #
# # if name == 'BM. Ashiq':
# #     print('Hello BM. Ashiq')
# #
# # elif name == 'Kanon':
# #     print('Hello kanon')
# #
# # elif name == 'konon':
# #     print('Hello kanon')
# #
# # else:
# #     print("I don't know who you are!")
#
# # # Nested IF -------------------------------------------------------
#
# employee_name_list = ['Sagir', 'Royel', 'Kanon']
#
# employee = 'Kalam'
# leave_taken = 25
# leave_allowed = 40
#
# if employee in employee_name_list:
#     print('Yes, ' + employee + ' is an employee of Transcom')
#
#     if leave_taken > leave_allowed:
#         print('He has no leave left')
#     else:
#         print('He has leave left = ' + str(leave_allowed - leave_taken) + ' days')
# else:
#     print(employee + ' not an employee of Transcom.')
#


import functions as fun

result = fun.myfunc(10)
print(result)