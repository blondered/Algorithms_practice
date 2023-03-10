# queue (FIFO)
"""
Научитесь пользоваться стандартной структурой данных queue для целых чисел. Напишите программу, 
содержащую описание очереди и моделирующую работу очереди, реализовав все указанные здесь методы. 

Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную 
операцию. После выполнения каждой команды программа должна вывести одну строчку.

Возможные команды для программы:

push n
Добавить в очередь число n (значение n задается после команды). Программа должна вывести ok.

pop
Удалить из очереди первый элемент. Программа должна вывести его значение.

front
Программа должна вывести значение первого элемента, не удаляя его из очереди.

size
Программа должна вывести количество элементов в очереди.

clear
Программа должна очистить очередь и вывести ok.

exit
Программа должна вывести bye и завершить работу.

Перед исполнением операций front и pop программа должна проверять, содержится ли в очереди хотя бы 
один элемент. Если во входных данных встречается операция front или pop, и при этом очередь пуста, 
то программа должна вместо числового значения вывести строку error.

Формат ввода
Вводятся команды управления очередью, по одной на строке

Формат вывода
Требуется вывести протокол работы очереди, по одному сообщению на строке
"""

from sys import stdin


class Queue:
    values = []
    len = 0
    head = 0

    def push(self, n):
        self.values.append(n)
        self.len += 1
        print("ok")

    def pop(self):
        if self.len == 0:
            print("error")
            return
        self.len -= 1
        print(self.values[self.head])
        self.head += 1
        if self.head > 1000:
            self.values = self.values[self.head :]
            self.head = 0

    def front(self):
        if self.len == 0:
            print("error")
            return
        print(self.values[self.head])

    def size(self):
        print(self.len)

    def clear(self):
        self.values = []
        self.len = 0
        self.head = 0
        print("ok")

    def exit(self):
        print("bye")
        exit(0)


def main():
    queue = Queue()
    while True:
        command = stdin.readline().strip()
        if command.startswith("push"):
            queue.push(int(command.split()[-1]))
        elif command == "pop":
            queue.pop()
        elif command == "front":
            queue.front()
        elif command == "size":
            queue.size()
        elif command == "clear":
            queue.clear()
        elif command == "exit":
            queue.exit()


if __name__ == "__main__":
    main()
