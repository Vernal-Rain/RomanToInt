from roman_to_int import roman_int, int_roman

if __name__ == '__main__':
    option = input('Would you like to convert from (a)roman numeral to integer or (b)integer to roman numeral?')
    if option == 'a' or option == 'A':
        numeral = input("Please enter roman numeral: ")
        print(numeral, '=', roman_int(numeral.upper()))
    elif option == 'b' or option == 'B':
        integer = int(input("Please enter integer: "))
        print(integer, '=', int_roman(integer))
    else:
        print('Invalid input')

