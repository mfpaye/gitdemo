# Snail Sort from Codewars
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
# This image will illustrate things more clearly:


# note: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

# note 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].



#take each item in the first array and add to a new list
def first_shell(array):
    new_list = []
    first_line = array.pop(0)
    for item in first_line:
        new_list.append(item)

#take the last item from each remaining set of items.
    for line in array:
        if line == []:
            pass
        else:
            last_item = line.pop(-1)
            new_list.append(last_item)
#
# Add the last line in reverse
    if array == []:
        pass
    else:
        array[-1].reverse()
        last_line = array.pop(-1)
        for item in last_line:
            new_list.append(item)


#take the first item of the remaining list, 
# add them to a list, 
# reverse their orders, then add them the new list.
    intermedite_list = []
    for line in array:
        if line == []:
            pass
        else:
            first_item_in_list = line.pop(0)
            intermedite_list.append(first_item_in_list)
    intermedite_list.reverse()
    for digit in intermedite_list:
        new_list.append(digit)
    # print(f'new_list:{new_list} \narray:{array}')

    return new_list, array

#Now repeat this process till the list is empty
def snail(array):
    final_new_list =[]
    for line in array:
        print(line)
    while len(array)!=0:
        result, array = first_shell(array)
        for item in result:
            if item == []:
                pass
            else:
                final_new_list.append(item)
    return final_new_list



# Example Arrays
array = [[1, 2, 4, 6], [4, 5, 6,7], [8, 9, 10,11]]
array1 = [[],[]]
array2 = [[1, 2, 4, 6], [4, 5, 6,7], [8, 9, 10,11], [12, 13, 14, 15]]
array3 = [
    [1, 2, 3, 4, 5],
[6, 7, 8, 9, 10],
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25]
]
x = snail(array3)
print(x)

    # print(f'new_list:{new_list} \narray:{array}')



#######################################################################
#######################################################################
#######################################################################

###############
1
###############
### easier way to do this:
import numpy as np

def snail(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m


###############
2
###############
# my implementation/explanation of the solution by foxxyz
def snail(array):
  if array:
    # force to list because zip returns a list of tuples
    top_row = list(array[0])
    # rotate the array by switching remaining rows & columns with zip
    # the * expands the remaining rows so they can be matched by column
    rotated_array = zip(*array[1:])
    # then reverse rows to make the formerly last column the next top row
    rotated_array = rotated_array[::-1]
    return top_row + snail(rotated_array)
  else:
    return []



###############
3
###############
def snail(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1] # Rotate
    return out


###############
4
###############
def snail(array):
    res = []
    while len(array) > 1:
        res = res + array.pop(0)
        res = res + [row.pop(-1) for row in array]
        res = res + list(reversed(array.pop(-1)))
        res = res + [row.pop(0) for row in array[::-1]]
    return res if not array else res + array[0]



###############
4
###############
snail = lambda a: list(a[0]) + snail(zip(*a[1:])[::-1]) if a else []
