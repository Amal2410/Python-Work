text="The quick brown fox jumps over a lazy dog"

text=text.casefold()

alphabets="abcdefghijklmnopurstuvwxyz"

is_panagram=True

for ch in alphabets:

    if text.count(ch)==0:

        is_panagram=False

        break

print(is_panagram)


