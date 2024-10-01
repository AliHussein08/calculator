def calculator():
    print('''what is operation would you to do?
    subtraction
    plus
    division
    multiply
    ''')


def calculate():
    operation = input('please write to me').lower()
    x = int(input('send a number: '))
    y = int(input('send other number: ')) 
         
    if operation == 'plus':
        print(x + y)
    else: print('erro')
    if operation == 'subtraction':
        print(x - y)
    else: print('errou')
    if operation == 'division':
        print(x/y)
    else: print('erro')
    if operation == 'multiply':
        print(x * y)
    else: print('error')
 
def again():
    while True:
        calculator()
        calculate()


        novo = input('well, would you like use calculator again? say yes to use or not.').lower()
        if novo != 'yes':
            print('thank you')
            break

again()