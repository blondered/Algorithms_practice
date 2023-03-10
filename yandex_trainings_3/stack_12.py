# stack (LIFO)

"""
Рассмотрим последовательность, состоящую из круглых, квадратных и фигурных скобок. 
Программа дожна определить, является ли данная скобочная последовательность правильной. 
Пустая последовательность явлется правильной. Если A – правильная, то последовательности 
(A), [A], {A} – правильные. Если A и B – правильные последовательности, то последовательность 
AB – правильная.

Формат ввода
В единственной строке записана скобочная последовательность, содержащая не более 100000 скобок.

Формат вывода
Если данная последовательность правильная, то программа должна вывести строку yes, иначе строку no.
"""

from sys import stdin


def main(line):
    len_line = len(line)
    if len_line == 0:
        print("yes")
        return
    if len_line % 2 != 0:
        print("no")
        return
    stack = []
    len_stack = 0
    openings = ["(", "{", "["]
    matching = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    for symbol in line:
        if symbol in openings:
            stack.append(symbol)
            len_stack += 1
        elif len_stack == 0:
            print("no")
            exit(0)
        else:
            if matching[symbol] != stack[-1]:
                print("no")
                return
            else:
                stack.pop()
                len_stack -= 1
    if len(stack) == 0:
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    line = stdin.readline().strip()
    main(line)
