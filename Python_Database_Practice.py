from vars import *  # this will expose all the variables in vars.py

list_of_answers=[]   # initializes the list

list_of_answers.append(len(some_numbers))   # appends however many objects there are in some_numbers to the list of answers

# adds the numbers in some_numbers and appends them to list of answers
sum_numbers = sum(some_numbers)
list_of_answers.append(sum_numbers)

list_of_answers.append(len(student['courses']))   # appends however many objects there are in student to the list of answers

list_of_answers.append(student['birthdate'])   # appends the birthdate of the student

# initializes red_cars and then starts a loop to count however many red cars there are in towed_cars and then appends the amount to list of answers
red_cars = 0
for i in range(len(towed_cars)):
  if towed_cars[i].get('color') == 'RED':
    red_cars += 1
list_of_answers.append(red_cars)

# initializes sil_4d_cars and then starts a loop to count however many four door silver cars there are in towed_cars and then appends the amount to list of answers
sil_4d_cars = 0
for i in range(len(towed_cars)):
  if towed_cars[i].get('color') == 'SIL' and towed_cars[i].get('style') == '4D':
    sil_4d_cars += 1
list_of_answers.append(sil_4d_cars)

# a new list is initliazed to get all of the inventory numbers from the loop and then appends the max of those numbers to list of answers
check_list = []
for i in range(len(towed_cars)):
  check_list.append(int(towed_cars[i]['inventory_number']))
list_of_answers.append(max(check_list))

list_of_answers.append(len(course_catalog['BIOS100']))   # appends the number of objects in course_catalog to list of answers

# uses a loop to print out the different objects of list of answers
for i in range(len(list_of_answers)):
  print(str(i + 1) + '.', list_of_answers[i])

# prints the dictionary course_catalog in alphabetical order by the keys
for key in sorted(course_catalog.keys()):
  print('%s: %s' % (key, course_catalog[key]))
