char_array = map(chr, range(97, 123))
n = 1
alphabet = {}

for a in char_array:
    alphabet[a] = n
    n += 1

def answer(names):
    words = {}

    for name in names:
        total = 0

        for char in name:
            total += alphabet[char]

        words[name] = total

    lexicagraphical_sort = sorted(names)
    sorted_names = sorted(lexicagraphical_sort, key=words.__getitem__)

    previous_value = 0
    unsorted = []
    output = []

    for name in sorted_names:
        if words[name] == previous_value:
            unsorted.append(name)

        elif len(unsorted) != 0:
            output += unsorted
            unsorted = []

            output.append(name)
        else:
            output.append(name)

        previous_value = words[name]


    output += unsorted

    return output[::-1]
