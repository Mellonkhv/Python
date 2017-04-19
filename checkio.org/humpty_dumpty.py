from math import pi, asin, log, sqrt


def checkio(height, width):
    height, width = height/2, width/2
    a = 0
    b = 0
    if height == width:
        a = float(4 * pi * (width ** 2))
        b = float((4 / 3) * pi * (width ** 3))
    else:
        b = (4 * pi / 3) * (width ** 2) * height
        if height > width:
            a = 2 * pi * width * (
            width + (height ** 2 / sqrt(height ** 2 - width ** 2)) * asin(sqrt(height ** 2 - width ** 2) / height))
        else:
            a = 2 * pi * width * (width + (height ** 2 / sqrt(width ** 2 - height ** 2)) * log(
                (width + sqrt(width ** 2 - height ** 2)) / height))
    return [round(b, 2), round(a, 2)]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"