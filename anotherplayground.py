#course can be found: https://cs50.harvard.edu/x/2023/psets/1/credit/
#  Multiply every other digit by 2, starting with the number’s second-to-last digit, 
# and then add those products’ digits together.
# Add the sum to the sum of the digits that weren’t multiplied by 2.
# If the total’s last digit is 0 (or, put more formally, if the total modulo 10 
# is congruent to 0), the number is valid!

#All American Express numbers start with 34 or 37; most MasterCard numbers start 
# with 51, 52, 53, 54, or 55 (they also have some other potential starting numbers 
# which we won’t concern ourselves with for this problem); and all Visa numbers start with 4. 

#redit card numbers also have a “checksum” built into them, a mathematical relationship 
# between at least one number and others. That checksum enables computers (or humans who like math) 
# to detect typos (e.g., transpositions), if not fraudulent numbers, without having to query 
# a database, which can be slow. Of course, a dishonest mathematician could certainly craft 
# a fake number that nonetheless respects the mathematical constraint, so a database lookup 
# is still necessary for more rigorous checks.
# test visa card number: 4003600000000014
#wrong number = 4123456789012

#-----------------------------------------------------
#first try of checksym

def checksum(credit_card_number):
    credit_card_number = str(credit_card_number)

    #grab every other digit by 2, starting with the number’s second-to-last digit
    odd_reversed = credit_card_number[-2::-2]

    #grab every other digit by 2, starting with the number’s last digit
    remaining_digits = credit_card_number[-1::-2]
    sums = 0

    #Multiply each number in odd_reversed by two then add to the sum.
    # then add the sums of the digits together 
    for digit in odd_reversed:
      for subdigit in str(int(digit) * 2):
        sums += int(subdigit)

    #add the remaining digits to the sums
    for otherdigit in remaining_digits:
        sums += int(otherdigit)
    return sums


#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
#--------------------------------------------------
#Ask user to enter their credit card number
def enter_credicardnumber():
    credit_card_number = input('Please enter a credit card number: \n')
    return credit_card_number

#--------------------------------------------------
#Check to make sure they entered numbers only
def numbers_only(credit_card_number):
    for digit in credit_card_number:
        if digit.isdigit():
            pass
        else:
            return False
    return True
#-----------------------------------------------
#Check that they entered a valid number
def check_cc_numbs(credit_card_number):
    credit_card_checklist = [ 
        [[15], 'American Express', '34', '37'],
        [[16], 'MasterCard', '51', '52', '53', '54', '55' ],
        [[13, 16], 'VISA', '4']
        ]
    for eachitem in credit_card_checklist:
        if len(credit_card_number) in eachitem[0]:
            if credit_card_number[0] in eachitem or credit_card_number[0:2] in eachitem:
                return f'Card Type: {eachitem[1]}'
    else:
        return False
         
#-----------------------------------------------

def checksum2(credit_card_number):
    credit_card_number = credit_card_number[::-1]
    counter = 0
    sums = 0
    for digits in credit_card_number:
        if counter % 2 != 0:
           for sub_digit in str(int(digits) * 2):
            sums += int(sub_digit)
        else:
            sums += int(digits)
        counter += 1
    if sums % 10 == 0:
        return True
    else:
        return False
        
#-----------------------------------------------
#compilation of the functions
def credicardverification():
    while True:
        credit_card_number_set = enter_credicardnumber()
        for credit_card_number in credit_card_number_set:
            if numbers_only(credit_card_number):
                result = check_cc_numbs(credit_card_number)
            else:
                print('Error 001: You can only enter numbers. Please reenter your credit card number.\n \n \n')
                continue

            if result == False: 
                print('Error 002: Invalid credit card number. Please reenter your credit card number. \n \n \n')
                continue
            else:
                if checksum2(credit_card_number):
                    return f"""
                    Valid credit card number.
                    Credit card: {credit_card_number}
                    {result} """
                    break
                else:
                    print('Error 003: Your credit number is not correct. \nPlease verify and enter the correct numbers.\n \n \n')
                    continue


x = credicardverification()
print(x)