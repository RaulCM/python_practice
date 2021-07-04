def len_of_longest_pall_subseq(s, left, right, memo):
    if left > right:
        return 0

    if left == right:
        return 1

    if (left, right) in memo:
        return memo[(left, right)]

    ans = 0
    if s[left] == s[right]:
        ans = 2 + len_of_longest_pall_subseq(s, left + 1, right - 1, memo)
    else:
        ans = max(len_of_longest_pall_subseq(s, left, right - 1, memo),
                len_of_longest_pall_subseq(s, left + 1, right, memo))

    memo[(left, right)] = ans
    return ans


s = "zkohwcuantjyteitydkiuufgtdiofgxwvpudjjkzxniquindjacsatncytsmrrxdrzmhbmknyhmkvthjqlmqwadylguyueosttzylbkqyauctvuyqdoaxomfuisfxffpagkibqyxbzuhslvpodwzvhmmalhjakirhlpnwwrxbdxhyhmdlaorrqabvsulbbqacfqqqskrnqcvektcwsuqbffcisehmpcsesqfeuonvojzpbzjqrnhvjmpznamxrhhxhrztfonjeegathvuoungfwyvmqucjnscrdcuszsxqaepjeltusdrfhtdkxckipqqgyxyhspgysfwvapjmpgalrnyvylhfavkolzynwcvmizlmabtrimfhztgdfdzpppfdzbiellpeillbzddfzpppyzlsfdzfmimrtgmbmlximcwcnbytzloviafhflvynhbrlagpjpvpuwsgshyxyprqcqpkxukdkthfrdsuutbjejpyenoaqxtsxbdcsnzcuqmgvywfntuuvotagejoofzrxhrxmnzrdpqvchnnrbrqpjonvofuuyfyqescimohbecsicfbdflbquswkevtcyqpnrsdqqftxabblusuvbaqrmqaromoslmhpyhdxhyrwwnplhqrkajhnlamhxvmgzwpelsghupzyqbilkrgapoffxfisufoxodrquyutcuqkbyztoeusuyunpgliydawqmjwlqjtkfhyxnkjmibmzdzxrrtoevstyclznlascajnvisulqinxzskjdvwxjnkfaoiogfuikhldptjieutxyjincwoz"
k = 216


# can you delete at most k characters such that after the deletion s is a palindrome.
l = len_of_longest_pall_subseq(s, 0, len(s) - 1, {})
print(k >= len(s) - l)
