# Basic Example -----------------------------------------------------
# number1 = 5
# number2 = 5
# if number1 > number2:
#     print(number1, ' is greater than', number2)
# else:
#     print(number2, ' is either smaller than or equal to = ', number1)


# # Example 2--------------------------------------------------------
# name = 'Kanon'
#
# if name == 'BM. Ashiq':
#     print('Hello BM. Ashiq')
# elif name == 'Kanon':
#     print('Hello kanon')
# else:
#     print("I don't know who you are!")

# # Nested IF -------------------------------------------------------

employee_name_list = ['Sagir', 'Royel', 'Kanon']
employee = 'Sagir'
leave_taken = 25
leave_allowed = 24

if employee in employee_name_list:
    print('Yes, ' + employee + ' is an employee of Transcom')

    if leave_taken > leave_allowed:
        print('He has no leave left')
    else:
        print('He has leave left = ' + str(leave_allowed - leave_taken) + ' days')
else:
    print(employee + ' not an employee of Transcom.')

