# 2 указателя
"""
Красотой строки назовем максимальное число идущих подряд одинаковых букв. (красота строки 
abcaabdddettq равна 3)

Сделайте данную вам строку как можно более красивой, если вы можете сделать не более k операций 
замены символа.

Формат ввода
В первой строке записано одно целое число k (0 ≤ k ≤ 109)

Во второй строке дана непустая строчка S (|S| ≤ 2 ⋅ 105). Строчка S состоит только из маленьких 
латинских букв.

Формат вывода
Выведите одно число — максимально возможную красоту строчки, которую можно получить.
"""
def main(k, S):

    len_s = len(S)
    ans = k
    for letter in "abcdefghijklmnopqrstuvwxyz":
        left = 0
        right = 0
        used = 0
        while left < len_s and right < len_s:
            ans = max(ans, right - left)
            if S[right] != letter:
                if used == k:
                    left += 1
                    while S[left-1] == letter:
                        left += 1
                else:
                    used += 1
            right += 1
    print(ans)


if __name__ == "__main__":
    k = int(input())
    S = input()
    main(k, S)
