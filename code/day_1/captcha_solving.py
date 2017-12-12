def varify(integer):
    integer = list(map(int, str(integer)))
    print(integer)
    summation = 0
    for index, i in enumerate(integer):

        try:
            if i == integer[index + 1]:
                summation += i
        except IndexError:
            if integer[-1] == integer[0]:
                summation += i

    return summation


# print(varify(1122))
# print(varify(1111))
# print(varify(1234))
# print(varify(91212129))
# print(varify(81112778))


def varify_other(integer):
    integer = list(map(int, str(integer)))
    print(integer)
    summation = 0
    len_half = int(len(integer)/2)
    for index, i in enumerate(integer):
        
        try:
            if i == integer[index + len_half]:
                summation += i
        except IndexError:
            # index + len_half is obviously greater than 
            new_ind = index - len_half 
            if i == integer[new_ind]:
                summation += i

    return summation


print(varify_other(1212))
print(varify_other(1221))
print(varify_other(123425))
print(varify_other(123123))
print(varify_other(12131415))
