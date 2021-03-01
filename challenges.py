def first():
    n = int((input("Input : ").strip()))
    if (n % 2 != 0) or (n % 2 == 0 and 6 <= n <= 20):
        print("Weird")
    elif (n % 2 == 0) and (2 <= n <= 5 or n > 20):
        print("Not Weird")


def second():
    a = int((input("Input : ").strip()))
    b = int((input("Input : ").strip()))
    print(a + b)
    print(a - b)
    print(a * b)


def third():
    a = int((input("Input : ")))
    b = int((input("Input : ")))
    print(a // b)
    print(a / b)


def fourth():
    a = int(input())
    start = 0
    while a >= start:
        print(start ** 2)
        start += 1


def is_leap(year):
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def print_on_same_line():
    a = int(input())
    n = 1
    while n <= a:
        print(n, sep='', end='')
        n += 1


def cube_challenge(x, y, z, n):
    all_permutations = [[a, b, c] for a in range(0, x + 1) for b in range(0, y + 1) for c in range(0, z + 1) if
                        a + b + c != n]
    print(all_permutations)


def find_runner_up():
    n = int(input())
    arr = map(int, input().split())
    mylist = set(arr)
    max_value = (list(mylist))[-1]
    print(max_value)


if __name__ == '__main__':
    find_runner_up()


