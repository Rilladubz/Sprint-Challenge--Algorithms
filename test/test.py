import string

alphabets = string.ascii_lowercase


def broken_eggs(n, *args):
    broken_eggs = 0
    thrown_eggs = 0
    for i in range(n):
        story_floor = {i: alphabets[i]}
        print(story_floor)

    for arg in args:
        if arg > 5:
            print(
                f'You threw an egg off of floor {arg} it will broke trying floors 5 and under will ensure it does not break')
            broken_eggs += 1
            thrown_eggs += 1
        elif arg <= 5:
            print(
                f'Since you threw an egg off of floor {arg} it did not break')
            thrown_eggs += 1

    return f'Broken eggs: {broken_eggs}, Thrown eggs: {thrown_eggs}'


print(broken_eggs(12, 1, 2, 4, 7, 9, 3))
