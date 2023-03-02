# heap

from sys import stdin


class Heap:
    values = []
    size = 0

    def print_tree(self):

        for node in range(self.size):
            left_child = self.get_left_child(node)
            right_child = left_child + 1
            left_value = self.values[left_child] if left_child < self.size else "-"
            right_value = self.values[right_child] if right_child < self.size else "-"
            print(self.values[node], ":", left_value, ", ", right_value)

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
        while self.is_child_too_big(node):
            left_child = self.get_left_child(node)
            switch_child = (
                left_child
                if self.values[left_child] > self.values[node]
                else left_child + 1
            )
            self.values[switch_child], self.values[node] = (
                self.values[node],
                self.values[switch_child],
            )
            node = switch_child

    def get_left_child(self, node):
        return 2 * node + 1

    def is_child_too_big(self, node):
        left_child = self.get_left_child(node)
        if left_child >= self.size:
            return False
        if left_child == self.size - 1:
            return self.values[node] < self.values[left_child]
        right_child = left_child + 1
        return self.values[node] < max(
            self.values[left_child], self.values[right_child]
        )

    def get_parent(self, node):
        return (node - 1) // 2

    def pop_max(self, return_value=False):
        answer = self.values[0]
        if not return_value:
            print(answer)
        self.size -= 1
        if self.size > 0:
            self.values[0] = self.values.pop()
            self.sift_down(0)
        else:
            self.values.pop()
        if return_value:
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
            heap.print_tree()
        else:
            heap.pop_max()
            heap.print_tree()


if __name__ == "__main__":
    main()
