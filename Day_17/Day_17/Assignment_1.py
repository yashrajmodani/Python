text = "abcdefabcddhABFDSHGWUIFCBvsASVBSNDUVWuiehnkjdbacxjam"

def remove_duplicate(text):
    res = ''
    seen = set()
    for char in text:
        if char not in seen:
            res += char
            seen.add(char)

    return res

print(remove_duplicate(text))


