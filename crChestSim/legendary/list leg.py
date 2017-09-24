import os

a = os.listdir()
for x in a:
    if ".py" in x:
        a.remove(x)

for x in a:
    if ".db" in x:
        a.remove(x)

end = []
for x in a:
    x_new = x.split(".png")
    x_new = "".join(x_new).replace(".png", "")
    end.append("\""+"".join(x_new)+"\"")

print(",".join(end))
