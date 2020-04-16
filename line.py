import matplotlib.pyplot as plt
from Connection import *


def plot(dr):
    plt.figure(figsize=(7,7))
    print(dr.patients)
    plt.title('Disease analysis', {'fontsize': 20, 'fontweight': 'bold'})
    monthName=['January','February','March','April','May','June','July','August','September','October','November','December']
    dispMonth=['Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec']
    count=[]
    query = '''SELECT 
                        MONTHNAME(date_of_entry),count((monthname(date_of_entry)))
                    FROM
                        entries
                    where
    	                monthname(date_of_entry)="%s" and patient_id in ('''
    ids=dr.patients.split(',')
    print(ids)
    for id in range(0,len(ids)):
        query+=str(ids[id])
        if(id!=(len(ids)-1)):
            query+=','
    query+=');'
    print(query)
    for month in monthName:
        result=analysePatients(query,month)
        count.append(result[0][1])
    print(count)
    plt.plot(dispMonth,count)
    plt.show()


if(__name__ == '__main__'):
    plot()
    #[3, 4, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0]