from sys import stdin
from heap_19 import Heap


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
    for i in range(len(numbers)):
        ans.append(heap.pop_max(return_value=True))
    print(*ans[::-1])


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    main(numbers)
