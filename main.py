#Python 2 need to import this for correct print() function
from __future__ import print_function


#Variable for my BFC (add comma in original code), can also do input() function for users
brainFuckCode = '>++++++++[<+++++++++>-]<.>>+>+>++>[-]+<[>[->+<<++++>]<<]>.+++++++..+++.' \
                '-------------------------------------------------------------------.' \
                '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>' \
                '->+++++++.<+[>[+>]>]<<<+++++++++++++++.>>.+++.------.--------.>>+.>++++.'


#Function find the brackets and return dictionary with {start:end, end:start} for ?????????????????????????????????????????
def bracket(brainFuckCode):
    opened = []
    brackets = {}
    for i in range(len(brainFuckCode)):
        if brainFuckCode[i] == '[':
            opened.append(i)
        elif brainFuckCode[i] == ']':
            brackets[i] = opened[-1]
            brackets[opened.pop()] = i
    return brackets


#Function that read the BFC and ??????????????????????????????????????????????
def main(brainFuckCode):
    cell = i = 0
    dictionary = {0: 0}
    brackets = bracket(brainFuckCode)
    length = len(brainFuckCode)
    print(brackets.items())

    while (i < length):
        symbol = brainFuckCode[i]
        if (symbol == '>'):
            cell = cell + 1
            dictionary.setdefault(cell, 0)
        elif (symbol == '<'):
            cell = cell - 1
        elif (symbol == '+'):
            dictionary[cell] = dictionary[cell] + 1
        elif (symbol == '-'):
            dictionary[cell] = dictionary[cell] - 1
        elif (symbol == '.'):
            print(chr(dictionary[cell]), end='')
        elif (symbol == ','):
            dictionary[cell] = int(input('Input number: '))
        elif (symbol == '['):
            if (not dictionary[cell]):
                i = brackets[i]
        elif (symbol == ']'):
            if (dictionary[cell]):
                i = brackets[i]
        i = i + 1
        print (dictionary[cell])

#Call main function
main(brainFuckCode)