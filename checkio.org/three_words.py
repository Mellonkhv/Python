def checkio(words):
    n = 0
    for text in words.split():
        if not text.isdigit():
            n += 1
            if n == 3:
                return True
        else:
            n = 0
    return False

print(checkio("start 5 one two three 7 end"))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"