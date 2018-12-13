input = "a"
append_end = True

def stringmover(input):
    string = "1"
    output = []
    for letter in input:
        if append_end is True:
            string = string+letter
            # string = string.append(letter)
        else:
            string = letter+string
                # string = string.insert(0, letter)
        append_end != append_end
    print(output)
    return output

ret_val = stringmover(input)
