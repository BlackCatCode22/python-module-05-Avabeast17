# word_count.py
# Count word frequencies in a text file and print the most common word.

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "clown.txt"

hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # idiom: retrieve/create/update counter
        di[w] = di.get(w, 0) + 1

# find the most common word (key) and its count (value)
largest = -1
theword = None
for k, v in di.items():
    if v > largest:
        largest = v
        theword = k

print(theword, largest)