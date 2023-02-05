# ____________________________________
#  1                                      
#  2   4   2                              
#  3   6   9   6   3                      
#  4   8   12  16  12  8   4             
#  5   10  15  20  25  20  15  10  5   
#  ___________________________________
 
# The total sum of the numbers in the triangle, 
# up to the 5th line included, is 225, 
# part of it, 144, corresponds to the total sum of the even terms 
# and 81 to the total sum of the odd terms.

# Create a function that may output an array with three results for each value of n.

# triang_mult(n)  ----> [total_sum, total_even_sum, total_odd_sum]
# Our example will be:

# triang_mult(5) ----> [225, 144, 81]


#  ______________________________________________________________________
# First Answer
#  ______________________________________________________________________

def triang_mult(n):
    number_of_lines = list(range(1,n+1))
    
    def multiplier(num):
        # Make a list of the numbers on each line and their reverse
        base_digit = number_of_lines + number_of_lines [:-1:-1] 
        return [num*each_numb for each_numb in base_digit] 

    ### calculate the final numbers for each line
    fwd_rev_lines = list(map(multiplier, number_of_lines))

    ### combine the numbers from each line into one list
    combined_list = []
    for line in fwd_rev_lines:
        combined_list += line

    ### Add everything
    total_sum = sum(combined_list)
    total_even_sum = 0
    total_odd_sum = 0
    for number in combined_list:
        if number%2==0:
            total_even_sum += number 
        else:
            total_odd_sum += number

    return total_sum, total_even_sum, total_odd_sum


x = 5
y = triang_mult(x)
print(y)




#  ______________________________________________________________________

# Second answer

#  ______________________________________________________________________
# def triang_mul_2 (n):
#     number_of_lines = list(range(1,n+1))
#     digit_per_line = list(range(1,n+1)) + list(range(1,n))[::-1]

#     for line in number_of_lines:


#  ______________________________________________________________________



# z = triang_mul_2(x)
# print(z)