txt = input("Enter a text: ").split(" ")
letter = []
txt = set(txt)
print(txt)

txt = list(txt)
for word in txt:
    for alpha in word:
        letter.append(alpha)

# letter =sorted(letter)
print(sorted(set(letter)))

