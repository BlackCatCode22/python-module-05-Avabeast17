# sort_dict_top5.py
# Print the top 5 most frequent words from a file.

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "clown.txt"

fhand = open(fname)
many = dict()

for line in fhand:
    line = line.rstrip()
    wds = line.split()

    for w in wds:
        many[w] = many.get(w, 0) + 1

# find the top 5 word frequency
tmp = dict()
newlist = list()

for k, v in many.items():
    tup = (v, k)
    newlist.append(tup)

cool = sorted(newlist, reverse=True)

# print the first 5 as "word count"
for v, k in cool[:5]:
    print(k, v)