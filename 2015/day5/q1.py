with open('constants.txt', 'r') as f:
    strings = [line.strip() for line in f]
vowels = set(['a', 'e', 'i', 'o', 'u'])
naughty_combos = ['ab', 'cd', 'pq', 'xy']
nice_count = 0
for string in strings:
    vowel_count = 0
    has_double = False
    past_letter = ''
    nice = True
    for letter in string:
        if letter == past_letter:
            has_double = True
        if letter in vowels:
            vowel_count += 1
        for combo in naughty_combos:
            if combo in string:
                nice = False
        past_letter = letter
    if vowel_count >= 3 and has_double and nice:
        nice_count += 1
print(nice_count)