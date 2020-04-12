import numpy as np
from matplotlib import pyplot as plt
from os import system


data = [int(input("Количество присутствующих: ")),int(input("Количество отсутствующих: ")),int(input("Количество опоздавших: "))]

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis("equal")
titles = ["В школе","отсувствуют","опоздавших"]
ax.pie(data,labels = titles,autopct = "%1.2f%%")
plt.show()
system('pause')