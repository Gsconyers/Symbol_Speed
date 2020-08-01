# In retrospect I am unsure why I used "symbols" instead of saying "characters"
import random
import time

char_to_use = "\\!@#$%^&*()-_+={}[];:\'\",.<>/?|"


# input string is a nonspaced string of all characters that should be included
# output is the generated string
def gen_a_string(input_string):
    char_list = list(char_to_use)
    length_of_list = len(char_list)
    # this will be how long the generated string is
    length_of_gen_string = random.randint(5, 10)
    # randomly selected characters are added to this list
    gen_string_list = []
    for x in range(0, length_of_gen_string):
        the_char = char_list[random.randint(0, length_of_list - 1)]
        gen_string_list.append(the_char)
    output_string = ""
    for char in gen_string_list:
        output_string += char
    return output_string

# This handles the length logic for the grader method
# returns the parameters that will be used for the loop and the errors
def length_check(o_len,t_len):
    errors = 0
    to_check = 0
    if o_len < t_len:
        # too long means all extra in the typed are errors, and check the first o_len
        # characters of the strings.
        errors = t_len - o_len
        to_check = o_len
    else:
        # too short means all missing are errors, and check the first t_len characters of
        # the strings. Note that equal lengths will be handled here as well.
        errors = o_len - t_len
        to_check = t_len
    results = {"errors":errors,"to check":to_check}
    return results
# grading compares the original and the input string and returns the errors

def grading(original,typed):
    print("grading")
    original_list = list(original)
    typed_list = list(typed)
    #for cleanliness, the lengths are stored.
    original_length = len(original_list)
    typed_length = len(typed_list)
    results = length_check(original_length,typed_length)
    error_count = results["errors"]
    positional_errors = []
    for char in range(0,results["to check"]):
        original_char = original_list.pop(0)
        typed_char = typed_list.pop(0)
        if original_char != typed_char:
            error_count += 1
            positional_errors.append(char)
    return {"errors":error_count,"positional_errors":positional_errors}
#TODO: implement graphical showing of where mistakes were made. Example:

# test
# tsett
#  ^^ ^


# driver. Should probably separate the final scores
def do_test():
    master_string = gen_a_string(char_to_use)
    mslen = len(master_string)
    print("please enter the string below as quickly as possible")
    print(master_string)
    start = time.time()
    user_input = input()
    end = time.time()
    total_time = end - start
    print(user_input)
    results = grading(master_string, user_input)
    error_count = results["errors"]
    position_of_mistakes = results["positional_errors"]
    percent_errors = (((mslen-error_count)-mslen)/mslen)
    if percent_errors <0:
        print("You made more mistakes than there are characters in the original string.")
        print("Pay better attention to what you are typing.")
    else:
        print("your accuracy was ", percent_errors,"%")
        print("you took", total_time, "seconds.")

    print(position_of_mistakes)
#do_test()

# what follows is some experiments on getting the positional error indication working

original = "12345"
wrong = "12XXX"
short = "1234"
long = "123456"
# instead of refactoring into proper method, change comp to change what is compared.
# todo: not this
comp = long
def largest_val(first,second):
    if first < second:
        return second
    else:
        return first

def largest_smallest(first,second):
    num_list = []
    if first < second:
        num_list.append(second)
        num_list.append(first)
    else:
        num_list.append(first)
        num_list.append(second)
    return num_list

#get output dictionary
test_output = grading(original,wrong)
#prove it worked
print(test_output["positional_errors"])
#put into list
positions = test_output["positional_errors"]
#initialize error positions
error_positions = ""
#get the pair sorted
ordered_vals = largest_smallest(len(original),len(comp))
print(ordered_vals)
#append the "position" of a missing/extra character
if len(original) != len(comp):
    for x in range(ordered_vals[1],ordered_vals[0]):
        positions.append(x)

    #add the carets to point at mistakes
for char in range(0,largest_val(len(original),len(comp))):
    if positions:
        if char == positions[0]:
            print("error found at position", char)
            error_positions += "^"
            positions.pop(0)
            print(positions)
        else:
            error_positions += " "
    else:
        error_positions += " "
# the idea here is that, by going with the longest length value, all errors would be covered
# regardless of whether it is too long or too short

print(original)
print(comp)
print(error_positions)
