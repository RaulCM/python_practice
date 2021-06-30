from collections import Counter


def min_win_substr(source, target):
    need = Counter(target)
    missing = len(need)

    ansBegin = len(source)
    ansEnd = ansBegin + len(source) + 2
    begin = 0
    for end, ch in enumerate(source):

        # grow from right by 1
        if ch in need:
            need[ch] -= 1
            if need[ch] == 0:
                missing -= 1

        # shrink from left as long as valid
        while missing == 0:
            ch1 = source[begin]
            if ch1 in need:
                need[ch1] += 1
                if need[ch1] > 0:
                    missing += 1

            if end - begin < ansEnd - ansBegin:
                ansBegin = begin
                ansEnd = end

            begin += 1

    return source[ansBegin : ansEnd + 1]


print(min_win_substr("abaa", "aa"))
