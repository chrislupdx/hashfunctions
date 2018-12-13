multiplier = 83
h = 9
testinput = 1705070271736160785
remainder = ""
letters = "acdekilmnoprstuy"


def number_to_letter_one(hash_value, letters):
    # print("OG hash_value is "+ str(hash_value))
    remainder = int(hash_value % multiplier)
    # print("remainder is", remainder)
    hash_value = (hash_value - remainder) // multiplier
    # print("numberinput after r is removed =", hash_value)
    current = letters[remainder]
    if hash_value == h:
        return letters[remainder]

    return number_to_letter_one(hash_value, letters) + letters[remainder]

ret_val = number_to_letter_one(testinput, letters)
print(ret_val)
