import matplotlib.pyplot as plt
from Connection import *


def draw():
    plt.figure(figsize=(7,7))
    plt.title('Disease analysis', {'fontsize': 20, 'fontweight': 'bold'})
    monthName=['January','February','March','April','May','June','July','August','September','October','November','December']
    dispMonth=['Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec']
    count=[]
    for month in monthName:
        result=analysePatients(month)
        count.append(result[0][1])
    print(count)
    plt.plot(dispMonth,count)
    plt.show()


if(__name__ == '__main__'):
    draw()