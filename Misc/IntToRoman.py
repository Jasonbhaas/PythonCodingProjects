def intToRoman(num):
    result = []

    M = num // 1000
    result.append("M" * M)
    num = num % 1000

    if num // 900 == 1:
        result.append("CM")
        num -= 900

    if num > 500:
        result.append("D")
        num -= 500

    if num // 400 == 1:
        result.append("CD")
        num -= 400

    C = num // 100
    result.append("C" * C)
    num = num % 100

    if num // 90 == 1:
        result.append("XC")
        num -= 90

    if num > 50:
        result.append("L")
        num -= 50

    if num // 40 == 1:
        result.append("XL")
        num -= 40

    X = num // 10
    result.append("X" * X)
    num = num % 10

    if num // 9 == 1:
        result.append("IX")
        num -= 9

    if num > 5:
        result.append("V")
        num -= 5

    if num // 4 == 1:
        result.append("IV")
        num -= 4

    result.append("I" * num)

    a = ''.join(result)

    b = 6


print(intToRoman(450))
