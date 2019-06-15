"""
Session 2:
1) Conditional statement
2) Looping Statement
"""

# if statement
'''
if <condition>:
    <statement_1>
    <statement_2>

if ...
 
if ... else ...

if ... elif ... else ...

if .. if .. elif ... else ...

'''

'''
number_01 = 3
number_02 = 3

if number_01 < number_02:
    print("Number 01 is minimum.")
elif number_02 < number_01:
    print("Number 02 is minimum.")
else:
    print("Both are same.")
'''

# number_01 = 3
# number_02 = 1
# number_03 = 1

# if number_01 == number_02 == number_03:
#     print("All numbers are same.")
#
#
# elif number_01 < number_02:
#     if number_01 < number_03:
#         print("Number 01 is minimum.")
#     elif number_01 == number_03:
#         print("Number 01 and Number 03 are minimum.")
#     else:
#         print("Number 03 is minimum.")
#
# else:
#     if number_02 < number_03:
#         print("Number 02 is minimum.")
#     elif number_02 == number_03:
#         print("Number 02 and Number 03 are minimum.")
#     else:
#         print("Number 03 is minimum.")
#
#
#
# if number_01 < number_02 and number_01 < number_03:
#     print("Number 01 is minimum.")
# elif number_02 < number_03:
#     print("Number 02 is minimum.")
# else:
#     print("Number 03 is minimum.")

#
# if number_01 == number_02 == number_03:
#     print("All numbers are same.")
#
# elif number_01 < number_02 <= number_03:
#     print("Number 01 is minimum.")
#
# elif number_01 <= number_02 < number_03:
#     print("Number 01 and Number 02 are minimum")
#
# elif number_01 == number_03 < number_02:
#     print("Number 01 and Number 03 are minimum")
#
# elif number_02 < number_03:
#     print("Number 02 is minimum.")
#
# elif number_02 == number_03:
#     print("Number 02 and Number 03 are minimum.")
#
# else:
#     print("Number 03 is minimum.")


# for
# while

'''
for iterator in <iterable_object>:
    <statement_1>
    <statement_2>

range(start, end, step)

'''
# for i in range(10, 1, -1):
#     print(i)
#
'''
while <condition>:
    <statement_1>
    <statement_2>
'''

# i = 1
# while i < 11:
#     print(i)
#     i += 1

# i = 1
# while True:
#     if i >= 11:
#         break
#     print(i)
#     i += 1

"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""

# for i in range(0, 5):
#     for j in range(0, 5):
#         print('*', end=" ")
#     print("\n")
