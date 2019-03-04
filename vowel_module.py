from collections import Counter

vowels = ['a', 'e', 'i', 'o', 'u']


def count_vowels(string):
    """
    Check how many vowels are in the string
    and how many times a duplicate of the vowel
    appears e.g. in nkoko, the function should
    return ('o', 2) since 'o' appears twice.
    """
    vowel_counter = Counter()
    char_list = []

    for char in string:
        if char in vowels:
            char_list.append(char)
            vowel_counter[char] += 1
    str_list = list(set(char_list))
    vowel_string = ''.join(str_list)

    duplicates = 0

    for value in vowel_counter.values():
        if value >= 2:
            duplicates += 1
    return (vowel_string, duplicates)
