# Python-Session-5---Assignment-2

Print the data in three lists in a specific order.

Subject = ["Americans", "Indians"]
Verb = ["play", "watch"]
Object = ["baseball", "cricket"]

for a in range(len(Subject)):
    for b in range(len(Verb)):
        for c in range(len(Object)):
            x = "%s %s %s." % (Subject[a], Verb[b], Object[c])
            print (x)
