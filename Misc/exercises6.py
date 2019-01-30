import math
digit = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5}

def stringToInt(s):
    negative = False
    val = 0
    for i in range(len(s)):
        if s[i] == '-':
            negative = True
        else:
            val = val * 10 + digit[s[i]]
        
    if negative:
        val = val * -1
    return val

print(stringToInt("123"))
print(stringToInt("-154"))
print(stringToInt("0"))


def intToString(i):
    if i == 0:
        return "0"
    neg = False
    if (i < 0):
        neg = True
        i = i * -1
    length = math.floor(math.log(i, 10)) + 1
    result = "0" * length
    for j in reversed(range(length)):
        result[j] = str(i % 10)
        i = i/10
    
    if neg:
        result = "-" + result
    return result

print(intToString(134))
print(intToString(-134))
print(intToString(0))
print(intToString(-1))

