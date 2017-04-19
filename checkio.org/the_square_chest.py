def checkio(lines_list):
    small = 0
    for i in range(len(lines_list)):
        lines_list[i] = sorted(lines_list[i])
    from_big = [[1, 2], [2, 3], [3, 4], [1, 5], [5, 9], [9, 13], [13, 14], [14, 15], [15, 16], [4, 8], [8, 12], [12, 16]]
    for i in range(1, 16):
        if lines_list.count([i, i+1]) and lines_list.count([i, i+4]) and lines_list.count([i+1, i+1+4]) and lines_list.count([i+4, i+1+4]):
            small += 1

        if lines_list.count([i, i+1]) and lines_list.count([i+1, i+2]) and lines_list.count([i, i+4]) and \
                lines_list.count([i+4, i+8]) and lines_list.count([i+2, i+6]) and lines_list.count([i+6, i+10]) \
                and lines_list.count([i+8, i+9]) and lines_list.count([i+9, i+10]):
            small += 1
    if all(x in lines_list for x in from_big):
        small += 1
    print(small)
    return small

if __name__ == '__main__':
    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"