proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.
# if ',' or ';' or ' ' in proto_list1:
#     print("True")
# else:
#     print("False")
# if ',' or ';' or ' ' in proto_list2:
#     print("True")
# else:
#     print("False")
# if ',' or ';' or ' ' in proto_list3:
#     print("True")
# else:
#     print("False")
# if ',' or ';' or ' ' in proto_list4:
#     print("True")
# else:
#     print("False")    

# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.
new_proto_list1 = proto_list1.split(',')
new_reversed_list1 = new_proto_list1[::-1]
final_list1 = ','.join(new_reversed_list1)
print(final_list1)

# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.
new_proto_list2 = proto_list2.split(';')
sorted_list2 = sorted(new_proto_list2)
final_list2 = ';'.join(sorted_list2)
print(final_list2)

# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.
new_proto_list3 = proto_list3.split(' ')
new_proto_list3.sort(reverse=True)
print(new_proto_list3)

# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.
