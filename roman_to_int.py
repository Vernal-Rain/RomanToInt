'''Roman numeral to integer, works for 1<=n<=3999'''
#Elaine Lee
#1/24/20 - updated 8/18/20


def roman_int(s:str) -> int:
    a = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    num = 0
    for i in range(len(s)-1):
        num += (1 if a[s[i]] >= a[s[i+1]] else -1) * a[s[i]]
    return num + a[s[-1]]
        
        
def int_roman(n:int) -> str: 
    a = {
        (3, 1): "M",
        (2, 5): "D",
        (2, 1): "C",
        (1, 5): "L",
        (1, 1): "X",
        (0, 5): "V",
        (0, 1): "I"  
    }
    string = ''
    while n > 0:
        i = len(str(n))-1
        num = n // 10**i
        n = n % 10**i

        if num == 9:
            string += a[(i, 1)] + a[(i+1, 1)]
        elif num < 9 and num > 4:
            string += a[(i, 5)] + a[(i, 1)]*(num-5)
        elif num == 4:
            string += a[(i, 1)] + a[(i, 5)]
        else:
            string += a[(i, 1)]*num
    return string

        






        
