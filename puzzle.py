letterinput = 'cloud'
letters = "acdekilmnoprstuy"

def letter_to_number(the_string):
    h = 9
    for x in range(len(the_string)):
        h = ((h * 83) + letters.index(the_string[x]))
        print(letters.index(the_string[x]))

    return h

ret_val = letter_to_number(letterinput)
print(ret_val)
assert ret_val == 35502317995
