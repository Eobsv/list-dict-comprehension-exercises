# new_list  = [new_item for item in list if test]

number = [1, 2, 3]
new_list = []
for n in number:
    add_1 = n
    new_list.append(add_1)

new_list2 = [n for n in number]
new_list3 = [n + 1 for n in number]

print(new_list)
print(new_list2)
print(new_list3)

name = "Genowefa"
letter_list = [letter for letter in name]
letter_list2 = [char for char in name]
numbers = [n for n in range(1, 5)]
numbers_m = [n * 2 for n in numbers]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Fred"]
short_names = [name for name in names if len(name) <= 4]
upper_longnames = [name.upper() for name in names if len(name) > 4]

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squarred_numbers = [number ** 2 for number in numbers]
print(squarred_numbers)
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

list2 = [3, 6, 13, 5, 7, 89, 12, 3, 33, 34, 1, 344, 42]
list1 = [3, 6, 5, 8, 33, 12, 7, 4, 72, 2, 42, 13]

common_numbers = [number for number in list1 if number in list2]
print(common_numbers)

# Dictionary comprehension
# new_dict = {new_key:new_value for item in list/dict}

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
# result = {word:len(word) for word in sentence.split()}
#
#
# print(result)
#


#
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
#
#
# # Write your code 👇 below:
# weather_f = {day:temp * 9 / 5 + 32 for (day, temp) in weather_c.items()}
#
#
# print(weather_f)

student_dict = {
    "student": ["Angela","James","Lily"],
    "score": [56,78,96]
}

for (key, value) in student_dict.items():
    print(key)
    print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

for (index, row) in student_data_frame.iterrows():
    #print(index)
    #print(row)
    #print(row.student)
    #print(row.score)
    if row.student == "Angela":
        print(row.score)
