import random

color_list = []
for i in range(0, 300):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand = (r, g, b)
    color_list.append(rand)
print(color_list)
