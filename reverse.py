numberinput = '35502317995'
letters = "acdekilmnoprstuy"
letters_to_numbers = enumerate(letters)
# print(letters_to_numbers)

def number_to_letter(number):
# does modulo return the first or last character?
    remainder = int(number) % 83
    number = int(number)
    print(remainder)
    word = (number - remainder) / 83


ret_val = number_to_letter(numberinput)
print(ret_val)
assert ret_val == cloud


    # for x in range(len(number)):
    # h = ((h / 83) - letters.index(number[x]))




    # the_string = (the_string-remainder)/83


#     return h
# assert ret_val == cloud
# h = 9
# for x in range(len(the_string)):
