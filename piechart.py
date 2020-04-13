import matplotlib.pyplot as plt
from Connection import *

def draw():
    plt.figure(figsize=(5,5))
    plt.title('Disease analysis',{'fontsize':20,'fontweight':'bold'})
    result = getEntries()
    values = []
    labels = []
    for ele in result:
        values.append(ele[1])
        labels.append(ele[0])
    explode = [0]*len(values)
    print(explode)
    max_value = max(values)
    index = values.index(max_value)
    explode[index]=0.05
    plt.axis('equal')
    plt.pie(values, labels=labels, radius=1, autopct='%0.2f%%', explode=explode)
    plt.show()


if __name__=='__main__':
    draw()