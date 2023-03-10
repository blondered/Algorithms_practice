# Hash table

"""
Лёша сидел на лекции. Ему было невероятно скучно. Голос лектора казался таким далеким и 
незаметным...

Чтобы окончательно не уснуть, он взял листок и написал на нём свое любимое слово. Чуть ниже он 
повторил своё любимое слово, без первой буквы. Ещё ниже он снова написал своё любимое слово, но в 
этот раз без двух первых и последней буквы.

Тут ему пришла в голову мысль — времени до конца лекции все равно ещё очень много, почему бы не 
продолжить выписывать всеми возможными способами это слово без какой-то части с начала и какой-то 
части с конца?

После лекции Лёша рассказал Максу, как замечательно он скоротал время. Максу стало интересно 
посчитать, сколько букв каждого вида встречается у Лёши в листочке. Но к сожалению, сам листочек 
куда-то запропастился.

Макс хорошо знает любимое слово Лёши, а ещё у него не так много свободного времени, как у его друга,
 так что помогите ему быстро восстановить, сколько раз Лёше пришлось выписать каждую букву.

Формат ввода
На вход подаётся строка, состоящая из строчных латинских букв — любимое слово Лёши.

Длина строки лежит в пределах от 5 до 100 000 символов.

Формат вывода
Для каждой буквы на листочке Лёши, выведите её, а затем через двоеточие и пробел сколько раз она 
встретилась в выписанных Лёшей словах (см. формат вывода в примерах). Буквы должны следовать в 
алфавитном порядке. Буквы, не встречающиеся на листочке, выводить не нужно.


"""


def main(word):
    count = {}
    limit = len(word)
    for i, letter in enumerate(word):
        if letter not in count:
            count[letter] = 0
        add = (i + 1) * (limit - i)
        count[letter] += add
    letters = sorted(count.keys())
    for letter in letters:
        print(letter, ": ", count[letter], sep="")


if __name__ == "__main__":
    word = input().strip()
    main(word)
