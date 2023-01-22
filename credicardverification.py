# credit card #: 4003600000000014

# Multiply every other digit by 2, starting with the number’s second-to-last digit, 
# and then add those products’ digits together.
# Add the sum to the sum of the digits that weren’t multiplied by 2.
# If the total’s last digit is 0 (or, put more formally, if the total modulo 10 
# is congruent to 0), the number is valid!

def creditcardvalidation():
    credit_card_numbs = input('Enter your credit card number: \n')
    # Define each credit card validation requirements
    # credit_card_numbs = str(credit_card_numbs)
    credit_card_set = [ 
        [[15], 'American Express', '34', '37'],
        [[16], 'MasterCard', '51', '52', '53', '54', '55' ],
        [[13, 16], 'VISA', '4']
        ]
    
    # Make sure the number of entered number is valid using teh criteria above. 
    # Length and first digits need to be correct.
    while True:
        counter = 0
        for aset in credit_card_set:
            if len(credit_card_numbs) in aset[0]:
                if int(credit_card_numbs[0]) in aset or int(credit_card_numbs[0:2]) in aset:
                    #verify that the digit add up correctly
                    listed = []
                    #convert each digit to an interger then add to a list
                    for eachdigit in credit_card_numbs:
                        listed.append(int(eachdigit))
                    
                    #reverse the list and separate into two different list. 
                    # Every other digit is intered in one of the 2 lists.
                    listed.reverse()
                    odd_reversed = listed[1::2]
                    even_reversed = listed[::2]
                    sums = 0
                    for n in odd_reversed:
                        new_odd = n * 2
                        for digit in str(new_odd):
                            sums += int(digit)
                    for othern in even_reversed:
                        sums += int(othern)
                    return f"The number is valid! \n Number: {credit_card_numbs} \n {aset[1]}" if sums % 10 == 0 else "Invalid Credit card!"
                    break
        else:
            print ("Invalid credit number")
            credit_card_numbs = input("Please enter a valid credit card number: \n")



####### test area
# credicardnumbers_list = [
#     378282246310005, 
#     371449635398431, 
#     378734493671000, 
#     30569309025904, 
#     6011111111111117, 
#     6011000990139424, 
#     3530111333300000, 
#     3566002020360505, 
#     2221000000000009,
#     2223000048400011,
#     2223016768739313,
#     5555555555554444,
#     5105105105105100,
#     4111111111111111,
#     4012888888881881,
#     4222222222222]

# for cc in credicardnumbers_list:
#     print(creditcardvalidation (cc))

x = creditcardvalidation ()
print(x)




# --------------
def creditcardvalidation(credit_card_numbs):
    reversed_cc = reversed(credit_card_numbs)