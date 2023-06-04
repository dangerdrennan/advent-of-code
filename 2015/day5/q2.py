import re

def is_nice(string):
    '''
    matches single char, followed by any single char, followed by exact first captured group (single char)
    '''
    if not bool(re.search(r'(.).\1', string)):
        return False
    '''
    matches any two chars, followed by 0 or any chars, followed by exact first captured group (two chars)
    '''
    if not bool(re.search(r'(..).*\1', string)):
        return False
    return True

with open('constants.txt', 'r') as f:
    strings = [line.strip() for line in f]

print(len([x for x in strings if is_nice(x)]))