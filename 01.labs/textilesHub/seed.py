"""
Seed stitch rectangle based on https://github.com/textiles-lab/knitout-examples/blob/master/seed.js
"""

# The yarn to use
Carrier = '1'
# The size of the rectangle
Width = 30
Height = 30
# The seed stitch pattern
Pattern = [
    'fb',
    'bf'
]

# Header
print(";!knitout-2")
print(";;Carriers: 1 2 3 4 5 6 7 8 9 10")

# Set the range of needles used
min_n = 1
max_n = min_n + Width - 1

# Cast on
print("x-stitch-number 61")
print(f"inhook {Carrier}")
for n in range(max_n, min_n - 1, -1):
    if (max_n - n) % 2 == 0:
        print(f"knit - f{n} {Carrier}")
for n in range(min_n, max_n + 1):
    if (max_n - n) % 2 != 0:
        print(f"knit + f{n} {Carrier}")
for n in range(max_n, min_n - 1, -1):
    print(f"knit - f{n} {Carrier}")
print(f"releasehook {Carrier}")

print("x-stitch-number 94")

# Build the pattern
needles = ['f'] * (max_n - min_n + 1)
for r in range(Height):
    pattern_row = Pattern[len(Pattern) - 1 - (r % len(Pattern))]
    target = [pattern_row[s % len(pattern_row)] for s in range(max_n - min_n + 1)]

    for n in range(min_n, max_n + 1):
        if needles[n - min_n] != target[n - min_n]:
            print(f"xfer {needles[n - min_n]}{n} {target[n - min_n]}{n}")
    needles = target

    if r % 2 == 0:
        for n in range(min_n, max_n + 1):
            print(f"knit + {needles[n - min_n]}{n} {Carrier}")
    else:

        for n in range(max_n, min_n - 1, -1):
            print(f"knit - {needles[n - min_n]}{n} {Carrier}")

# Move the stitches back to the front bed before dropping
for n in range(min_n, max_n + 1):
    if needles[n - min_n] != 'f':
        print(f"xfer {needles[n - min_n]}{n} f{n}")

print(f"outhook {Carrier}")

# Drop the stitches
for n in range(min_n, max_n + 1):

    print(f"drop f{n}")

