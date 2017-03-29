def recall_password(cipher_grille, ciphered_password):

    password=""

    for g in range(4): #For turning the grille
        for i in range(4): #row
            for j in range(4): #col
                if cipher_grille[i][j] == "X":
                    password+=ciphered_password[i][j]
        cipher_grille = tuple(zip(*cipher_grille[::-1])) #turns the grille 90 degrees clockwise

    return password


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
