def is_palindrome(word):
    for idx in range(len(word) // 2):
        if word[idx] == word[len(word) - idx - 1]:
            idx += 1
        else:
            return False
    return True


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
