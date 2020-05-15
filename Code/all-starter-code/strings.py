#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    if find_index(text, pattern) is not None:
        return True
    else:
        return False

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    start = 0
    index = 0
    index_pattern = 0
    #if pattern empty returns 0
    #You could also do it with the len(pattern) == 0
    if pattern == '':
        return 0
    while index < len(text):
        if text[index] == pattern[index_pattern]:
            index += 1
            index_pattern += 1
            # They all matches so return the start which is index
            if index_pattern == len(pattern):
                return start
        else:
            start += 1
            index = start
            index_pattern = 0
    return None

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    if len(pattern) == 0:
        return list(range(len(text)))

    index = find_index(text, pattern)
    index_list = []

    if index != None:
        index_list.append(index)

        index += 1
        start = index
        index_pattern = 0

        while index < len(text):
            if text[index] == pattern[index_pattern]:
                index += 1
                index_pattern += 1

                if index_pattern == len(pattern):
                    index_list.append(start)
                    index_pattern = 0
                    start += 1
                    index = start

            else:
                index_pattern = 0
                start += 1
                index = start
        return index_list
    return index_list


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
