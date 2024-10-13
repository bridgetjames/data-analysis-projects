my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.
new_string = my_string[3:]+my_string[0:3]
print(new_string)

# Use a template literal to print the original and modified string in a descriptive phrase.
# print("The original string reads as", my_string, "and the modified string reads as", new_string)
print("The original string reads as {0}, and the modified string reads as {1}.".format(my_string, new_string))

# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
num_letters_relocated = input('User Entry: ')
print(num_letters_relocated)
# use this to convert string to integer: int(num_letters_relocated)
new_string = my_string[int(num_letters_relocated):]+my_string[0:int(num_letters_relocated)]

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
if int(num_letters_relocated) > 10:
    print('User input cannot be longer than word.')
else:
    print(new_string)
