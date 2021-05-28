
from collections import Counter

def minWindow(source, target):
    need = Counter(target)
    missing = len(target)

    minBegin = 0
    minEnd = -1
    begin = 0
    # invariant win is invalid
    for end, ch in enumerate(source):
        # keep increasing win right
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1 # un-needed goes -ve

        # found a valid win
        if missing == 0:
            # keep decreasing win to right, skipping un-needed
            while begin < end and need[source[begin]] < 0:
                need[source[begin]] += 1
                begin += 1

            # update result
            if minEnd < 0 or end - begin < minEnd - minBegin:
                minBegin = begin 
                minEnd = end

            # skip leftmost needed to make win invalid again
            need[source[begin]] += 1
            missing += 1
            begin += 1

    return source[minBegin:minEnd+1]



s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))
