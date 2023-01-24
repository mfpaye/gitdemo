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
    # if array[0] == []:
    #     pass
    # else:
    #     first_line = array.pop(0)
    #     for item in first_line:
    #         new_list.append(item)
  
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

#Print the last line in reverse
    array[-1].reverse()
    last_line = array.pop(-1)
    for item in last_line:
        new_list.append(item)
    print(f'new_list:{new_list} \narray:{array}')

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
        reversed(intermedite_list)
        for digit in intermedite_list:
            new_list.append(digit)
    # print(f'new_list:{new_list} \narray:{array}')

    return new_list, array

#Now repeat this process till the list is empty
def snail_sort(array):
    new_list =[]
    for line in array:
        print(line)
    while len(array)!=0:
        result, array = first_shell(array)
        for item in result:
            if item == []:
                pass
            else:
                new_list.append(item)
    return new_list



# Example Arrays
array = [[1, 2, 4, 6], [4, 5, 6,7], [8, 9, 10,11]]
array1 = [[],[]]
array2 = [[1, 2, 4, 6], [4, 5, 6,7], [8, 9, 10,11], [12, 13, 14, 15]]
x = snail_sort(array2)
print(x)

    # print(f'new_list:{new_list} \narray:{array}')

