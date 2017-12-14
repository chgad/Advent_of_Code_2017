


def spiral(x):
    # x is the number we are asked to produce step counts
    # Therfore we need to know in which row/circle the number is,
    # how many steps there are on one edge and how many steps we did 
    # in the row/circle allready.

    row_len = 1
    row = 0
    number = 1
    row_steps = 0
    steps_in_row = 0
    while (x != number):
        if steps_in_row == row_steps:
            # enter a new row/circle
            row += 1
            row_len += 2
            row_steps = (row_len -1)*4 -1
            
            steps_in_row = 0
            number +=1
        else:
            # count forwards
            steps_in_row += 1
            number += 1

    return steps_in_row, row_len, row

def determine(steps_in_row, row_len , row):
    # we wannt the Manhattan Distance form our number to the number 1
    
    steps_to_middle = row-1
    
    for i in range(4):
        diff = steps_in_row - (i+1)*(row_len-1)
        # here we try to find out on which of the 4 edges the number sits
        # 0 being the edge when we enter a new circle, then counting to 3 counter-clockwise
        if diff < 0:
            # print(diff,i)

            # i symobolizes the edge of it
            any_middle = i*(row_len-1) + steps_to_middle
            # print(any_middle)
            if steps_in_row == any_middle:
                # if we are in the middle we only need to go directly to 1
                return row # due to the intelligent choice of the row indexation
            extra_steps = steps_in_row - any_middle
            # print(extra_steps)
            if extra_steps <0:
                return row + (-extra_steps)
            return row + extra_steps

steps_in_row, row_len, row = spiral(312051)

print(determine(steps_in_row=steps_in_row, row_len=row_len, row=row))

#print("entered 2",spiral(2))
#print("entered 4",spiral(4))
#print("entered 11",spiral(11))

