#!/usr/bin/env python3
import operator
from clint.textui import colored

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow
}

def color(number):
    if number < 0:
        return colored.red(number)
    else:
        return colored.black(number)

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            stack.append(int(token))
        except ValueError:
            print(color(stack[0]) + ' ' + color(stack[1]) + ' ' + colored.blue(token))
            arg2 = stack.pop()
            arg1 = stack.pop()
            function = ops[token]
            result = function(arg1, arg2)
            stack.append(result)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(raw_input("rpn calc> "))
        print('Result: ' + color(result))

if __name__ == '__main__':
    main()

