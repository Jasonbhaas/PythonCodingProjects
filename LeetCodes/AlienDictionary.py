def isAlienSorted(self, words: List[str], order: str) -> bool:
    d = {}  # for easy lookup of character's ranking
    for i in range(len(order)):
        d[order[i]] = i

    def w1_greater_than_w2(w1, w2, d):
        min_len = min(len(w1), len(w2))
        for i in range(min_len):
            c1 = w1[i]
            c2 = w2[i]
            if d[c1] > d[c2]:
                return True
            elif d[c1] < d[c2]:
                return False
        return len(w1) > len(w2)

    for i in range(len(words) - 1):
        if w1_greater_than_w2(words[i], words[i+1]):
            return False

    return True
