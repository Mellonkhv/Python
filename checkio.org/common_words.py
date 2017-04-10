def checkio(first_words, second_words):
    lists = sorted(list(set(first_words.split(",")) & set(second_words.split(","))))
    words = ""
    if len(lists) != 0:
        words = ",".join(lists)
    return words

if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "hello"
    assert checkio("one,two,three", "four,five,six") == "", ""
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "one,three,two"