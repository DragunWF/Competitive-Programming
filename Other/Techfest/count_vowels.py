s = input()
vowel_count = 0
VOWELS = "aeiou"
for char in s:
    if char in VOWELS:
        vowel_count += 1
print(vowel_count)
