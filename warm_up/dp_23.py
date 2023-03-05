# dynamic programming
"""
Имеется калькулятор, который выполняет следующие операции:

умножить число X на 2;
умножить число X на 3;
прибавить к числу X единицу.
Определите, какое наименьшее количество операций требуется, чтобы получить из числа 1 число N.

Формат ввода
Во входном файле написано натуральное число N, не превосходящее 106.

Формат вывода
В первой строке выходного файла выведите минимальное количество операций. Во второй строке выведите 
числа, последовательно получающиеся при выполнении операций. Первое из них должно быть равно 1, а 
последнее N. Если решений несколько, выведите любое.
"""

def main(N):
    if N == 1:
        print(0)
        print(1)
        return
    di = {N: (0, [N])}
    ans = N
    ans_history = [N]
    while di:
        new_di = {}
        for num, history in di.items():
            prev_count, prev = history
            for var in (2, 3):
                new_num = num // var
                new_count = num % var + 1 + prev_count
                    
                if (
                    new_num == 0
                    or new_count >= ans
                    or (new_num in new_di and new_count >= new_di[new_num][0])
                ):
                    continue

                new_history = list(prev)
                for _ in range(num % var):
                    new_history.append(new_history[-1]-1)
                new_history.append(new_num)

                if new_num > 1:
                    new_di[new_num] = (new_count, new_history)
                    
                elif new_count < ans:
                    ans = new_count
                    ans_history = new_history

        di = new_di

    print(ans)
    print(*ans_history[::-1])



if __name__ == "__main__":
    N = int(input())
    main(N)
