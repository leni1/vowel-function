from vowel_module import count_vowels


def test_func_return_tuple():
    result = count_vowels('chicken')
    assert isinstance(result, tuple)


def test_vowels_in_return_tuple():
    result = count_vowels('recommend')
    assert ('eo', 1) == result
