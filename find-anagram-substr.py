from collections import Counter


def collect_anagram_substrs(source, pattern):
    need = Counter(pattern)

    win_size = len(pattern)
    tally = Counter(source[:win_size])
    ans = []
    if need == tally:
        ans.append(0)

    for right in range(win_size, len(source)):
        cin = source[right]
        tally[cin] += 1
        left = right - win_size
        cout = source[left]
        tally[cout] -= 1

        if len(need - tally) == 0:
            ans.append(left + 1)

    return ans


print(collect_anagram_substrs("aababac", "ab"))
