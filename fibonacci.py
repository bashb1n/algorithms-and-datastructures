#!/usr/bin/env python

def fib(n):
    """ computes and returns the Nth fibonacci number:
       1 1 2 3 5 8 ...
       if n = 2; returns 1
       if n = 5; returns 5
       etc.
    """
    if n <= 2:
        return 1
    prev = 1
    prev_minus_one = 1
    for i in range(3, n + 1):
        cur = prev + prev_minus_one
        prev_minus_one = prev
        prev = cur
    return cur


def main():
    """ the main method """
    n = 5
    fib_n = fib(n)
    print(fib_n)
    assert fib_n == 5
    print("n=5  fib(n)={0}".format(fib_n))
    n = 6
    fib_n = fib(n)
    print(fib_n)
    assert fib_n == 8
    print("n=6  fib(n)={0}".format(fib_n))


if __name__ == "__main__":
    main()
