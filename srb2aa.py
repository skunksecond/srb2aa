import os

alist = [a for a in os.listdir("addons") if os.path.isfile(os.path.join("addons", a))]

print(alist)

try:
    f = open("autoexec.cfg", "x+")
except(FileExistsError):
    f = open("autoexec.cfg", "r+")

for a in alist:
    f.write("\n" + "addfile " + a)

f.close()


