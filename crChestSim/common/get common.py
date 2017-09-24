import os

a = os.listdir()
for x in a:
    if ".py" in x:
        a.remove(x)



end = []
for x in a:
    x_new = str(x).split(".png")
    end.append("<img id=\""+str("".join(x_new))+"\" scr=\"https://djpiper28.github.io/crChestSim/common/"+str("".join(x_new))+".png\" width=\"0\" height=\"0\"><img/>")

print("\n".join(end))
