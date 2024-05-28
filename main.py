def count_words(contents):
    words = contents.split()
    return len(words)

def count_chars(contents):
    counts = {}
    for c in contents.lower():
        if not c.isalpha():
            continue

        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1
    return counts

def report(filename):
    with open(filename) as f:
        contents = f.read()

    print(f"--- Begin report on {filename} ---")
    print(f"{count_words(contents)} words found in the document")
    print()

    counts = count_chars(contents)
    counts_dicts = []
    for c in counts:
        counts_dicts.append({"c": c, "count": counts[c]})

    def sort_on(cd):
        return cd["count"]

    counts_dicts.sort(reverse=True, key=sort_on)
    for cd in counts_dicts:
        print(f"The {cd["c"]} character was found {cd["count"]} times")

    print(f"--- End report ---")

report("books/frankenstein.txt")
