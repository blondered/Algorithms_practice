# heap
"""
В этой задаче вам необходимо самостоятельно (не используя соответствующие классы и функции 
стандартной библиотеки) организовать структуру данных Heap для хранения целых чисел, над которой 
определены следующие операции: a) Insert(k) – добавить в Heap число k ; b) Extract достать из Heap 
наибольшее число (удалив его при этом).

Формат ввода
В первой строке содержится количество команд N (1 ≤ N ≤ 100000), далее следуют N команд, каждая в 
своей строке. Команда может иметь формат: “0 <число>” или “1”, обозначающий, соответственно, 
операции Insert(<число>) и Extract. Гарантируется, что при выполнении команды Extract в структуре 
находится по крайней мере один элемент.

Формат вывода
Для каждой команды извлечения необходимо отдельной строкой вывести число, полученное при выполнении 
команды Extract.
"""


class Heap:
    values = []
    size = 0

    def get_left_child(self, node):
        return 2 * node + 1

    def get_parent(self, node):
        return (node - 1) // 2

    def sift_up(self, node):
        parent = self.get_parent(node)
        while node > 0 and self.values[parent] < self.values[node]:
            self.values[parent], self.values[node] = (
                self.values[node],
                self.values[parent],
            )
            node = parent
            parent = self.get_parent(node)

    def sift_down(self, node):
        while True:
            left_child = self.get_left_child(node)
            if left_child >= self.size:
                break
            son = left_child
            if (
                left_child + 1 < self.size
                and self.values[left_child] < self.values[left_child + 1]
            ):
                son += 1  # right child exists and is bigger the left
            if self.values[son] > self.values[node]:
                self.values[node], self.values[son] = (
                    self.values[son],
                    self.values[node],
                )
                node = son
            else:
                break

    def pop_max(self):
        answer = self.values[0]
        self.size -= 1
        if self.size > 0:
            self.values[0] = self.values.pop()
            self.sift_down(0)
        else:
            self.values.pop()
        return answer

    def insert(self, n):
        self.values.append(n)
        node = self.size
        self.size += 1
        self.sift_up(node)


def main():
    heap = Heap()
    n = int(input())
    for i in range(n):
        command = input()
        if command.startswith("0"):
            heap.insert(int(command.split()[1]))
        else:
            print(heap.pop_max())


if __name__ == "__main__":
    main()
