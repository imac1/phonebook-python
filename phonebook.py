import re

# Do not modify this list
phone_list = ["98-777-653", "98-742-644", "34-855-326", "34-25-629", 
              "34-489-115", "72-999-563", "9-321-459",
              "72-654-121", "72-4-694", "72-255-313", "98-111-323",
              "98-433-14", "34-577-342", "98-323-000",
              "98-202-666", "34-5435-454", "34-515-633"]              
good_phone_list = []
bad_phone_list = []
numbers_with_AC = []
numbers_without_AC = []
area_98 = []
area_72 = []
area_34 = []

# "These are the valid phone numbers in your phonebook:"
# "and these are the wrong ones:"

for value in phone_list:
    if re.match("^[\d0-9]{2}-[\d0-9]{3}-[\d0-9]{3}$", value):
        good_phone_list.append(value)
    else:
        bad_phone_list.append(value)

print('These are the valid phone numbers in your phonebook:' + str(good_phone_list) + "\n")
print("and these are the wrong ones:" + str(bad_phone_list) + "\n")

# "The area codes:"
# "and the numbers without the area codes:"

for value in good_phone_list:
    numbers_with_AC.append(value[0:2])
    numbers_without_AC.append(value[3:10])
print("The area codes:" + str(numbers_with_AC) + "\n")
print("and the numbers without the area codes:" + str(numbers_without_AC) + "\n")


# "The unique area codes:"
unique_AC = set(numbers_with_AC)
print("The unique area codes: " + str(unique_AC) + "\n")
# "You have X numbers from area 98, Y numbers from area 34,
# and Z numbers from area 72."
sum_1 = 0
sum_2 = 0
sum_3 = 0
for value in good_phone_list:
    numeric_value = int(value[0:2]) 
    if numeric_value == 98:
        sum_1 += 1
    elif numeric_value == 34:
        sum_2 += 1
    elif numeric_value == 72:
        sum_3 += 1

print(f"You have {sum_1} numbers from area 98")
print(f"You have {sum_2} numbers from area 34")
print(f"You have {sum_3} numbers from area 72")

# cu sum(list)

# for value in good_phone_list:
#     numeric_value = int(value[0:2])
#     if numeric_value == 98:
#         sum(area_98.append(value))      
# print(sum(area_98.append(value)))

# print(f'you have {sum(area_98.append(value))} in Area 98')