# deque (double ended queue) with blocks

"""
Научитесь пользоваться стандартной структурой данных deque для целых чисел.  Напишите программу, 
содержащую описание дека и моделирующую работу дека, реализовав все указанные здесь методы. 
Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную 
операцию. После выполнения каждой команды программа должна вывести одну строчку.

Возможные команды для программы:

push_front n
Добавить (положить) в начало дека новый элемент. Программа должна вывести ok.

push_back n
Добавить (положить) в конец дека новый элемент. Программа должна вывести ok.

pop_front
Извлечь из дека первый элемент. Программа должна вывести его значение.

pop_back
Извлечь из дека последний элемент. Программа должна вывести его значение.

front
Узнать значение первого элемента (не удаляя его). Программа должна вывести его значение.

back
Узнать значение последнего элемента (не удаляя его). Программа должна вывести его значение.

size
Вывести количество элементов в деке.

clear
Очистить дек (удалить из него все элементы) и вывести ok.

exit
Программа должна вывести bye и завершить работу.

Гарантируется, что количество элементов в деке в любой момент не превосходит 100. Перед исполнением 
операций pop_front, pop_back, front, back программа должна проверять, содержится ли в деке хотя бы 
один элемент. Если во входных данных встречается операция pop_front, pop_back, front, back, и при 
этом дек пуст, то программа должна вместо числового значения вывести строку error.

Формат ввода
Вводятся команды управления деком, по одной на строке.

Формат вывода
Требуется вывести протокол работы дека, по одному сообщению на строке


"""

from sys import stdin


class Deque:
    blocks = [[-1] * 100]
    front_block = 0
    front_index = -1
    back_block = 0
    back_index = 0
    deque_size = 0

    def push_front(self, n):
        self.deque_size += 1
        self.front_index += 1
        if self.front_index == 100:
            self.front_index = 0
            self.front_block += 1
            if len(self.blocks) >= self.front_block:
                self.blocks.append([-1] * 100)
        self.blocks[self.front_block][self.front_index] = n
        if self.deque_size == 1:
            self.back_block = self.front_block
            self.back_index = self.front_index
        print("ok")

    def push_back(self, n):
        self.deque_size += 1
        self.back_index -= 1
        if self.back_index == -1:
            self.back_index = 99
            self.back_block -= 1
            if self.back_block == -1:
                new_blocks = [[-1] * 100]
                new_blocks.extend(self.blocks)
                self.blocks = new_blocks
                self.back_block += 1
                self.front_block += 1
        self.blocks[self.back_block][self.back_index] = n
        if self.deque_size == 1:
            self.front_block = self.back_block
            self.front_index = self.back_index
        print("ok")

    def pop_front(self):
        if self.deque_size == 0:
            print("error")
            return
        self.deque_size -= 1
        print(self.blocks[self.front_block][self.front_index])
        self.front_index -= 1
        if self.front_index == -1 and self.deque_size > 0:
            self.front_index = 99
            self.front_block -= 1

    def pop_back(self):
        if self.deque_size == 0:
            print("error")
            return
        self.deque_size -= 1
        print(self.blocks[self.back_block][self.back_index])
        self.back_index += 1
        if self.back_index == 100:
            self.back_index = 0 if self.deque_size > 0 else -1
            self.back_block += 1

    def front(self):
        if self.deque_size == 0:
            print("error")
            return
        print(self.blocks[self.front_block][self.front_index])

    def back(self):
        if self.deque_size == 0:
            print("error")
            return
        print(self.blocks[self.back_block][self.back_index])

    def size(self):
        print(self.deque_size)

    def clear(self):
        self.blocks = [[-1] * 100]
        self.front_block = 0
        self.front_index = -1
        self.back_block = 0
        self.back_index = 0
        self.deque_size = 0
        print("ok")


def main():
    deque = Deque()
    while True:
        command = stdin.readline().strip()
        if command == "clear":
            deque.clear()
        elif command == "size":
            deque.size()
        elif command == "front":
            deque.front()
        elif command == "back":
            deque.back()
        elif command == "exit":
            print("bye")
            exit(0)
        elif command == "pop_front":
            deque.pop_front()
        elif command == "pop_back":
            deque.pop_back()
        else:
            command_list = command.split()
            command = command_list[0]
            n = int(command_list[1])
            if command == "push_front":
                deque.push_front(n)
            else:
                deque.push_back(n)


if __name__ == "__main__":
    main()
