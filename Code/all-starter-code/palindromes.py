#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    empty_string = ''
    for letter in text.lower():
      if string.ascii_lowercase.find(letter) >= 0:
          empty_string += letter

    left_index = 0
    right_index = len(empty_string) - 1

    while left_index < right_index:
      if empty_string[left_index] != empty_string[right_index]:
        return False
      left_index += 1
      right_index -= 1
    return True
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    empty_string = ''
    for letter in text.lower():
      if string.ascii_lowercase.find(letter) >= 0:
          empty_string += letter
    if left is None and right is None:
        left = 0
        right = len(empty_string) - 1

    # Three base cases
    if len(empty_string) == 0:
        return True
    elif empty_string[left] != empty_string[right]:
        return False
    elif right == 0:
        return True
    else:
        return is_palindrome_recursive(empty_string, left+1, right-1)
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
