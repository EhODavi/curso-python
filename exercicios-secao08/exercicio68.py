def intercala(str1: str, str2: str) -> str:
    str3: str = ''

    for i in range(max(len(str1), len(str2))):
        if i < len(str1):
            str3 += str1[i]
        if i < len(str2):
            str3 += str2[i]

    return str3
