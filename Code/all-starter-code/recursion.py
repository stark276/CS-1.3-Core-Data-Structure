#!python

def factorial(n):
    """factorial(n) returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n"""
    if not isinstance(n, int) or n < 0:
        raise ValueError('factorial is undefined for n = {}'.format(n))
    # implement factorial_iterative and factorial_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return factorial_iterative(n)
    return factorial_recursive(n)


def factorial_iterative(n):
    # TODO: implement the factorial function iteratively here
    result = 1
    for num in range(1, n+1):
        result = result * num

    return result


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return n * factorial_recursive(n - 1)


def main():
    import sys
    args = sys.argv[1:]
    if len(args) == 1:
        num = int(args[0])
        result = factorial(num)
        print('factorial({}) => {}'.format(num, result))
    else:
        print('Usage: {} number'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
