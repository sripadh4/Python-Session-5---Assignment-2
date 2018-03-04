
# coding: utf-8

# In[27]:

Subject = ["Americans", "Indians"]
Verb = ["play", "watch"]
Object = ["baseball", "cricket"]

for a in range(len(Subject)):
    for b in range(len(Verb)):
        for c in range(len(Object)):
            x = "%s %s %s." % (Subject[a], Verb[b], Object[c])
            print (x)

