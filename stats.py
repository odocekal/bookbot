def word_count(str):
    words = str.split(sep=None, maxsplit=-1)
    counter = len(words)
    return counter

def character_count(text):
    word_styling = text.lower()
    character_amount = {}

    for char in word_styling:
        if char in character_amount:
            character_amount[char] += 1
        else:
            character_amount[char] = 1
    return character_amount

def _sort_key(item):
    return item["num"]

def sort_char_counts(counts):
    chars = []
    for k, v in counts.items():
        if k.isalpha():
            chars.append({"char": k, "num": v})
    chars.sort(reverse=True, key=_sort_key)
    return chars

