# (x, y) = (44, "Fred")

# print(x)
# print(type(x))

# print(y)
# print(type(y))

# d = dict()

# d["csev"] = 2
# d["cwen"] = 4

# for (key, val) in d.items():
#     print(key, val)

# tups = d.items()
# print(tups)

# d = {"a" :10, "c" :1, "b" :22}
# t = sorted(d.items())
# print(t)

# for key, val in sorted(d.items()):
#     print(key, val)

c = {"a" :10, "b" :1, "c" :22}
tmp = list()

for key, val in c.items():
    tmp.append( (val, key) )

tmp = sorted(tmp, reverse=True)
print(tmp)
