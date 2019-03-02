'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''


def nice_function(x):
    print(f"i'm quite enjoying the {x}")


print(nice_function("functions"))


def bitcoin_price(price):
    if price >= 5000:
        return "sell"
    for price in range(3500, 4999):
        return "hodl"
    else:
        return "buy"


print(bitcoin_price(2800))


list_ = []


def third_function(k):
    flag = True
    while flag:
        for k in range(1, 1000001):
            k **= k
            list_.append(k)
            if k >= 900000:
                return list_


print(third_function(1))





