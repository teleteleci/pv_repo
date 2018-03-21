def find_in_text(text, char):
    cnt = 0
    for c in text:
        if c == char:
            cnt += 1
    return cnt


with open("a.yml") as f:
    text = f.read()


for char in "abcde":
    perc = 100 * find_in_text(text, char) / len(text)
    print("{0}: {1}%".format(char, round(perc, 2)))
