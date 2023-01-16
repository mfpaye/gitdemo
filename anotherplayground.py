# credit card #: 4003600000000014

# Multiply every other digit by 2, starting with the number’s second-to-last digit, 
# and then add those products’ digits together.
# Add the sum to the sum of the digits that weren’t multiplied by 2.
# If the total’s last digit is 0 (or, put more formally, if the total modulo 10 
# is congruent to 0), the number is valid!

def creditcardvalidation(credit_card_numbs):
    credit_card_set = [ 
        [[15], 'American Express', 51, 52, 53, 54, 55],
        [[16], 'MasterCard', 34, 37],
        [[13, 16], 'VISA', 4]
        ]


    
    while True:
        if type(credit_card_numbs) == int:
            credit_card_numbs = str(credit_card_numbs)
        while True:
            for aset in credit_card_set:
                if len(credit_card_numbs) in aset[0]:
                    if credit_card_numbs[0] in aset or credit_card_numbs[0:2] in aset:
                        print(aset[1])
                        break
                    else:
                        print(f'incorrect beginning {credit_card_numbs[0:2]}')
                else:
                    print(f'incorrect number of digits {len(credit_card_numbs)}')   
            else:
                print ("Invalid credit number")
                credit_card_numbs = input("Please enter a valid credit card number: \n")


    # listed = []
    # for item in credit_card_numbs:
    #     listed.append(int(item))
    # listed.reverse()
    # odd_reversed = listed[1::2]
    # even_reversed = listed[::2]
    # sums = 0
    # for n in odd_reversed:
    #     new_odd = n * 2
    #     for digit in str(new_odd):
    #         sums += int(digit)
    # for othern in even_reversed:
    #     sums += int(othern)
    # return "The number is valid!" if sums % 10 == 0 else "Invalid Credit card!"

print(len('4003600000000014'))
x = creditcardvalidation ('4003600000000014')
print(x)




# --------------
def creditcardvalidation(credit_card_numbs):
    reversed_cc = reversed(credit_card_numbs)
