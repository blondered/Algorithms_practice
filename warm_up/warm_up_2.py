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

    len_s = len(S)
    ans = k
    for letter in "abcdefghijklmnopqrstuvwxyz":
        for start in range(len_s-k):
            pretty = 0
            now = start
            used = 0
            while now < len_s:
                if S[now] != letter:
                    if used == k:
                        break
                    used += 1
                pretty += 1
                now += 1
            ans = max(ans, pretty)

    print(ans)



if __name__ == "__main__":
    k = int(input())
    S = input()
    main(k, S)
