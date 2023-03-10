# heap
# heap sort
"""
Отсортируйте данный массив. Используйте пирамидальную сортировку.

Формат ввода
Первая строка входных данных содержит количество элементов в массиве N, N ≤ 105. Далее задаются N 
целых чисел, не превосходящих по абсолютной величине 109.

Формат вывода
Выведите эти числа в порядке неубывания.
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


def heapify(numbers):
    heap = Heap()
    heap.values = numbers
    heap.size = len(numbers)
    node = len(numbers) // 2
    while node >= 0:
        heap.sift_down(node)
        node -= 1
    return heap


def main(numbers):
    heap = heapify(numbers)
    ans = []
    for _ in range(len(numbers)):
        ans.append(heap.pop_max())
    print(*ans[::-1])


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    main(numbers)
