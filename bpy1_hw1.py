a = 5.4 / 2
b = 5.4 // 2
c = 5.4 % 2
d = (3 + 4) % 3
e = 3 + 4 % 3
f = 2 ** 3 * 2
g = 2 + 5 * 3
h = 2 * 3 ** 2
i = (2 * 3) ** 2
j = - 1 + 5 * 3

combined = ['a = 5.4 / 2',
'b = 5.4 // 2',
'c = 5.4 % 2',
'd = (3 + 4) % 3',
'e = 3 + 4 % 3',
'f = 2 ** 3 * 2',
'g = 2 + 5 * 3',
'h = 2 * 3 ** 2',
'i = (2 * 3) ** 2',
'j = - 1 + 5 * 3']

tobecalculated = [a, b, c, d,e,f,g,h,i,j]
def calculator(a_list, an_list):
    for each in range(len(an_list)):
        print(an_list[each])
        each_item = str(round(a_list[each],2))
        player1 = input(f'Marietou, enter your guess:\n')
        player2 = input(f'Dan, enter your guess:\n')
        if each_item == player1 == player2:
            print('Marietou and Dan got the correct answer!')

        elif each_item == player1 :
            print('Marietou got the correct answer!')
           
        elif each_item == player2 :
            print('Dan got the correct answer!')

        else:
            print('Neither Marietou nor Dan got the correct answer!')

        print(f'The correct answer is {each_item}')
        print('*'*10)
        print('\n')



calculator(tobecalculated, combined)