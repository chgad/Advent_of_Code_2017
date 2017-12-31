def find_max(alist):
    maximum = alist[0]
    for entry in alist:
       if entry > maximum:
            maximum = entry
    index = alist.index(maximum)
    return maximum, index

 


def redistribution(string):

    banks = list(map(int,string.split()))
    encountered_config = []
    cycles = 0
    while not banks in encountered_config: 
        encountered_config.append(list(banks)) # after a redisttibution is done we add it to this list
        maximum, index = find_max(banks)
        banks[index] = 0
        index +=1 # we start at the next index
        while maximum > 0 :
            if index == 16 : # we want to start at the beginning once we hit the end
                index = 0
            banks[index] += 1
            index += 1
            maximum -= 1
        cycles += 1
    return cycles

test = "0  2  7  0"
# print(redistribution(test), "should print 5") to use this change Line 23 to 4 instead of 16
puzzel_input = "14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4"
print(redistribution(puzzel_input))




