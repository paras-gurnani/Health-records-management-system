from pymysql import *
from patients import *

def getPatient(id=10,dob='2000-6-10'):
    conn = connect(host="127.0.0.1", database="hospital", user="root", password='password')
    # print("connected")
    curr = conn.cursor()
    query = "select * from hospital.patients where patient_id=%d and dob='%s'"
    param=(id,dob)
    curr.execute(query%param)
    result = curr.fetchone()
    if(result==None):
        return None
    current_patient=Patients(id=result[0],name=result[1],age=result[2],gender=result[3],email=result[4],phone_number=result[5],dob=result[6])
    curr.close()
    conn.close()
    return current_patient

def getEntries(id=1):
    conn=connect(host="127.0.0.1",database="hospital",user="root",password='password')
    curr=conn.cursor()
    query="select * from hospital.entries where patient_id=%d"
    param=(id,)
    curr.execute(query%param)
    result=curr.fetchall()
    print(result)
    curr.close()
    conn.close()

def insertData(patient):
    conn=connect(host="127.0.0.1",database="hospital",user="root",password='password')
    curr=conn.cursor()
    query="insert into hospital.patients(full_name,age,gender,email,phone_no,dob) values('%s',%d,'%s','%s','%s','%s')"
    params=(patient.name,patient.age,patient.gender,patient.email,patient.phone_number,patient.dob)
    curr.execute(query%params)
    curr.close()
    conn.close()


# getPatient()
# getEntries()