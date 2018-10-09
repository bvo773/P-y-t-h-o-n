'''
n = 3
*
* *
* * *
'''


def pattern_1(n):
    i = 0
    while (i < n):
        k = 0
        j = i + 1
        while (k < j):
            print('*', end=" ")
            k += 1
        print()
        i += 1


'''
n = 3
    *
  * *
* * *
'''


def pattern_2(n):
    i = 0


def main():
    n = 3
    pattern_1(n)
    reverse()


if __name__ == '__main__':
    main()
