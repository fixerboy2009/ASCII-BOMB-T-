import os, time
os.system('clear')
names = ["FRAMES/1.txt", "FRAMES/2.txt", "FRAMES/3.txt", "FRAMES/4.txt", "FRAMES/5.txt", "FRAMES/6.txt"]
frames = []

for name in names:
    with open(name,"r",encoding="utf8") as f:
        frames.append(f.readlines())
for i in range(99999999999999999999999):

    for frame in frames:
        print("".join(frame))
        time.sleep(1)
        os.system('clear')
