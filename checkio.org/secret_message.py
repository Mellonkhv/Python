def find_message(text):
    message = ""
    for ch in text:
        if 65 <= ord(ch) <= 90:
            message += ch
    return message

#!!! find_message = lambda text: ''.join(filter(str.isupper, text)) - Лучший вариант решения

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"