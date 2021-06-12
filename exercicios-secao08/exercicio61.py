from collections import Counter


def anagrama(string_a: str, string_b: str) -> bool:
    return Counter(string_a) == Counter(string_b)
