def factorial(num):
    res=1
    for i in range(1,num+1):
        res=res*i
    return res


print(factorial(5))


# count vowels in the given strings.
def count_vowels(hello): # parameter
    for i in hello:
        if i=="aeiou":
            print(i, f"is the vowel in {hello}")


count_vowels("salman") # arguments 

