'''
n = 3
*
* *
* * *
'''


def pattern(n):
    i = 0
    while (i < n):
        k = 0
        j = i + 1
        while (k < j):
            print('*', end=" ")
            k += 1
        print()
        i += 1


def main():
    n = 3
    pattern(n)


if __name__ == '__main__':
    main()
