txt = input()
res = txt.split(" ")
a = ""
for r in res:
    if len(r) > len(a):
        a = r
print(a)