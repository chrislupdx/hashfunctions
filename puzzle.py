# writing the hash function out in python was straight forward enought
letterinput = 'cloud'
numberinput = '35502317995'

key = "acdekilmnoprstuy"
def letter_to_number(the_string):
    h = 9
    multiplier = 83
    print("the value of h before letters are added and the function is run is " + str(h))
    print("multiplier is "+ str(multiplier))
    for x in range(len(the_string)):
        h = ((h * multiplier) + key.index(the_string[x]))
        print("the letter is " + str(the_string[x])+ " and it has an index value of " + str(key.index(the_string[x])))
        print(str(h) + " = " + str(the_string[x])+ "("+str(key.index(the_string[x]))+")" + ", " + str(h)+ "(add to next row's letter value and apply multiplier)")
    return h

ret_val = letter_to_number(letterinput)
print(ret_val)
assert ret_val == 35502317995

# when the multiplier in the equation is 1 instead of 83, it simply adds the translated letter value to the letters_to_numbers
# whent the multiplier is 1, pulling the sum apart for letters is
# when the multiplier in the equation is 2 instead of 83, it doubles the translated letter valuesself.
#
# below is my first attempt at reverse engineering the hash function
# numberinput = '35502317995'
# letters = "acdekilmnoprstuy"
# numberinput = enumerate(letters)
#
# def number_to_letter(number):
# remainder is most likely the last character
#     remainder = int(number) % 83
#     number = int(number)
#     print(letters.index(remainder)
#     pass
#     thing = (number - remainder) / 83
#
# def number_to_letter_one(numberinput):
#     h = 9
#     multiplier = 83
#
#
# I know that the phrase is 8-9 characters because I could divide the given sum of CLOUD (35502317995) by 83 eight times (down to 9.12093689664), if the sum can be multiplied that many times it implies at least that many characters in the phrase
#
#
#
# . I'm pretty sure that h = (h/83 - character) is likely a part of the decryption equation
