# Hash table
"""
Вовочка ломает систему безопасности Пентагона. Для этого ему понадобилось узнать, какие символы 
в секретных зашифрованных посланиях употребляются чаще других. Для удобства изучения Вовочка хочет 
получить графическое представление встречаемости символов. Поэтому он хочет построить гистограмму 
количества символов в сообщении. Гистограмма — это график, в котором каждому символу, встречающемуся
в сообщении хотя бы один раз, соответствует столбик, высота которого пропорциональна количеству 
этих символов в сообщении. 

Формат вывода:

      #   
     ##  
#########
!,Hdelorw

"""

from sys import stdin


def main(lines):
    symbols = {}
    for line in lines:
        for word in line.split():
            for letter in word:
                if letter not in symbols:
                    symbols[letter] = 0
                symbols[letter] += 1
    listed_symbols = []
    listed_numbers = []
    max_met = 1
    for symbol in sorted(symbols.keys()):
        listed_symbols.append(symbol)
        listed_numbers.append(symbols[symbol])
        max_met = max(max_met, listed_numbers[-1])
    for num_met in range(max_met, 0, -1):
        line = []
        for number in listed_numbers:
            if number >= num_met:
                line.append("#")
            else:
                line.append(" ")
        print(*line, sep="")
    print(*listed_symbols, sep="")


if __name__ == "__main__":
    lines = stdin.readlines()
    main(lines)
