# stack (LIFO)

"""
Научитесь пользоваться стандартной структурой данных stack для целых чисел. Напишите программу, 
содержащую описание стека и моделирующую работу стека, реализовав все указанные здесь методы. 
Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную 
операцию. После выполнения каждой команды программа должна вывести одну строчку. Возможные команды 
для программы:

push n
Добавить в стек число n (значение n задается после команды). Программа должна вывести ok.

pop
Удалить из стека последний элемент. Программа должна вывести его значение.

back
Программа должна вывести значение последнего элемента, не удаляя его из стека.

size
Программа должна вывести количество элементов в стеке.

clear
Программа должна очистить стек и вывести ok.

exit
Программа должна вывести bye и завершить работу.

Перед исполнением операций back и pop программа должна проверять, содержится ли в стеке хотя бы один
 элемент. Если во входных данных встречается операция back или pop, и при этом стек пуст, то 
 программа должна вместо числового значения вывести строку error.

Формат ввода
Вводятся команды управления стеком, по одной на строке

Формат вывода
Программа должна вывести протокол работы стека, по одному сообщению на строке


"""


from sys import stdin


class Stack(list):
    length = 0

    def not_empty(self):
        if self.length == 0:
            print("error")
            return False
        return True

    def proceed_command(self, full_command):
        read_args = full_command.split()
        command = read_args[0]
        if command == "exit":
            print("bye")
            exit(0)
        elif command == "push":
            print("ok")
            self.length += 1
            self.append(int(read_args[1]))
        elif command == "back":
            if self.not_empty():
                print(self[-1])
        elif command == "pop":
            if self.not_empty():
                print(self.pop())
                self.length -= 1
        elif command == "size":
            print(self.length)
        elif command == "clear":
            print("ok")
            self.length = 0
            self.clear()


def main():
    stack = Stack()
    commands = stdin.readlines()
    for command in commands:
        stack.proceed_command(command)


if __name__ == "__main__":
    main()
