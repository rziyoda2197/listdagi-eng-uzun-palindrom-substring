def longest_palindrom_substring(s):
    n = len(s)
    longest = ""

    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) > len(longest):
                longest = substring

    return longest

print(longest_palindrom_substring("babad"))  # "bab"
print(longest_palindrom_substring("cbbd"))  # "bb"
```

Kodda biz quyidagi narsalarni amalga oshiramiz:

1. String uzunligini hisoblaymiz.
2. Stringning har bir substringini tekshiramiz.
3. Har bir substringni chegaralangan (palindrom bo'lishi kerak) va uzunligi eng uzun substringdan katta bo'lsa, eng uzun substringga qo'shamiz.
4. Eng uzun substringni qaytaradi.
