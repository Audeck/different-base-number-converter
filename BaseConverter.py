import math
import string


def fromBaseToBase(original_base, original_number, final_base):
    number_string_list = []
    number_list = []
    helper = 0  # Helper/auxiliary number in decimal (used for logarithms and other operations)
    number_index = 1
    original_base = original_base
    original_number = str(original_number)
    final_base = final_base
    final_number = ""

    ## Preliminary checks
    if original_base > 25:
        return "Sorry, this program doesn't support Base 26+; maybe in the future though!"
    if final_base > 25:
        return "Sorry, this program doesn't support Base 26+; maybe in the future though!"
    if original_number == 0 or original_base == final_base:
        return "Your number {} in base {} is {} in base {}.".format(original_number, original_base, original_number, final_base)

    ## Logic
    if original_base != 10:
        for x in original_number:
            if x in string.ascii_uppercase:
                number_list.append(int(string.ascii_uppercase.index(x)) + 10)
            elif x in string.ascii_lowercase:
                number_list.append(int(string.ascii_lowercase.index(x)) + 10)
            else:
                number_list.append(int(x))

        for x in number_list:  # Checking if the input number is valid in the selected number system
            if x >= original_base:
                return "Sorry, your number doesn't seem to be supported by the number system you selected."

            helper += x*(original_base**(len(number_list) - number_index))    # Adding sequentially x*base^(character index) -> converts the number to base 10
            number_index += 1

    else:  # In case of base 10
        helper = int(original_number)

    number_string_list = []  # Empty lists to reuse
    number_list = []
    temp_log = int(math.log(helper, final_base))  # First logarithm value

    while temp_log >= 0:  # Very flimsy
        number_list.append(int(helper/(final_base**temp_log)))
        helper -= int(helper/(final_base**temp_log))*(final_base**temp_log)
        temp_log -= 1

    for x in number_list:
        if x > 9:
            number_string_list.append(string.ascii_uppercase[x - 10])
        else:
            number_string_list.append(str(x))

    final_number = final_number.join(number_string_list)

    return final_number


if __name__ == "__main__":
    original_base = int(input("What base number system are you converting from (2 for binary, 3 for terniary, etc.)? "))
    original_number = input("What is the number you want to convert? ")
    final_base = int(input("What base number system are you converting to (2 for binary, 3 for terniary, etc.)? "))
    finalNumber = fromBaseToBase(original_base, original_number, final_base)

    print("Your number {} (originally in base {}) is {} in base {}.".format(original_number, original_base, finalNumber, final_base))
