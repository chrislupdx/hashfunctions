
# def number_to_letter(number):
# # does modulo return the first or last character?
#     remainder = int(number) % 83
#     number = int(number)
#     print(letters.index(remainder)
#     thing = (number - remainder) / 83

multiplier = 83
h = 9
numberinput = '35502317995'
remainder = ""
letters = "acdekilmnoprstuy"
def number_to_letter_one(numberinput, letters):
    print("OG numberinput is "+ str(numberinput))
    remainder = int(numberinput) % 83
    print("remainder is " + str(remainder))
    numberinput = (int(numberinput) - int(remainder))/83
    print("numberinput after r is removed = "+ str(numberinput))
    def number_to_letter_one(self, numberinput, letters):
        if numberinput == 9:
            print("finished")
            return
    print("boom")
    return number_to_letter_one(numberinput, letters)
# letters.index()

ret_val = number_to_letter_one(numberinput)
print(ret_val)
