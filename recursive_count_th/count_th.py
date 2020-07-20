'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_helper(word, first_index, second_index, count_tracker):
    first = first_index
    second = second_index
    count = count_tracker

    if len(word) == 0:
        return count
    elif word[first:second] == 'th':
        count += 1
        first += 1
        second += 1
        return count_helper(word, first, second, count)
    elif word[first:second] != 'th' and second - 1 < len(word):
        first += 1
        second += 1
        return count_helper(word, first, second, count)
    elif second - 1 >= len(word):

        return count


def count_th(word):
    count = count_helper(word, 0, 2, 0)
    return count


print(count_th('abcthxyz'))
