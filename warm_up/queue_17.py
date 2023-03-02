# queue (FIFO) with circle buffer
"""
В игре в пьяницу карточная колода раздается поровну двум игрокам. Далее они вскрывают по одной 
верхней карте, и тот, чья карта старше, забирает себе обе вскрытые карты, которые кладутся под низ 
его колоды. Тот, кто остается без карт – проигрывает. Для простоты будем считать, что все карты 
различны по номиналу, а также, что самая младшая карта побеждает самую старшую карту ("шестерка 
берет туза"). Игрок, который забирает себе карты, сначала кладет под низ своей колоды карту первого 
игрока, затем карту второго игрока (то есть карта второго игрока оказывается внизу колоды). Напишите
 программу, которая моделирует игру в пьяницу и определяет, кто выигрывает. В игре участвует 10 
 карт, имеющих значения от 0 до 9, большая карта побеждает меньшую, карта со значением 0 побеждает 
 карту 9.

Формат ввода
Программа получает на вход две строки: первая строка содержит 5 чисел, разделенных пробелами — 
номера карт первого игрока, вторая – аналогично 5 карт второго игрока. Карты перечислены сверху 
вниз, то есть каждая строка начинается с той карты, которая будет открыта первой.

Формат вывода
Программа должна определить, кто выигрывает при данной раздаче, и вывести слово first или second, 
после чего вывести количество ходов, сделанных до выигрыша. Если на протяжении 106 ходов игра не 
заканчивается, программа должна вывести слово botva.
"""


from sys import stdin


class Cards:
    def __init__(self, cards):
        self.values = cards
        self.values.extend([-1] * 5)
        self.head = 0
        self.tail = 4

    def put_card(self):
        card = self.values[self.head % 10]
        self.head += 1
        return card

    def get_cards_check_winner(self, first_card, second_card):
        self.values[(self.tail + 1) % 10] = first_card
        self.values[(self.tail + 2) % 10] = second_card
        self.tail += 2
        if self.tail - self.head == 9:
            return True
        return False


def main(first, second):
    first_cards = Cards(first)
    second_cards = Cards(second)
    for i in range(1000000):
        first = first_cards.put_card()
        second = second_cards.put_card()
        if (first > second and not (first == 9 and second == 0)) or (
            first == 0 and second == 9
        ):
            is_winner = first_cards.get_cards_check_winner(first, second)
            if is_winner:
                print("first", i + 1)
                return
        else:
            is_winner = second_cards.get_cards_check_winner(first, second)
            if is_winner:
                print("second", i + 1)
                return
    print("botva")


if __name__ == "__main__":
    first = list(map(int, stdin.readline().split()))
    second = list(map(int, stdin.readline().split()))
    main(first, second)
