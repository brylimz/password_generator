# # average height--------------
# student_heights = input("input a  list of student heights\n").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
#     print(student_heights)
# total_height = 0
# for height in student_heights:
#     total_height += height
#     print(total_height)
#
# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
# print(number_of_students)
#
# average_height = round(total_height / number_of_students)
# print(average_height)

# High Score-------------------
# student_scores = input("input a list of student score\n").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
#     print(student_scores)
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
#         print(f"the highest score in the class is {highest_score}")

# # For loop with range-------------------
# for number in range(1, 11, 3):
#     print(number)
#
# total = 0
# for number in range (1, 101):
#     total += number
#     print(total)

# adding evens----------------------
# total = 0
# for number in range(2, 101, 2):
#     total += number
# print(total)
# total2 = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total2 += number
# print(total2)

# Fizz buzz------------------
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
