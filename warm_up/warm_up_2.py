class Maximum:
    value = 1

    @classmethod
    def check_maximum(self, new_maximum):
        self.value = max(self.value, new_maximum)


class Letter:
    def __init__(self, jokers_limit):
        self.num_met = 0
        self.jokers_used = 0
        self.jokers_limit = jokers_limit

    def add_meeting_different(self):
        if self.jokers_used == self.jokers_limit:
            Maximum.check_maximum(self.num_met)
            self.num_met = 0
            self.jokers_used = 0
            return
        self.jokers_used += 1
        self.num_met += 1

    def add_meeting_same(self):
        self.num_met += 1


def main(k, S):
    letters = {}
    for letter in S:
        if letter not in letters:
            letters[letter] = Letter(jokers_limit=k)
        letters[letter].add_meeting_same()
        for any_letter_key, any_letter_object in letters.items():
            if any_letter_key != letter:
                any_letter_object.add_meeting_different()
    for any_letter_object in letters.values():
        Maximum.check_maximum(
            any_letter_object.num_met + k - any_letter_object.jokers_used
        )
    print(min(Maximum.value, len(S)))


if __name__ == "__main__":
    k = int(input())
    S = input()
    main(k, S)
