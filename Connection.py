from pymysql import *
from patients import *


def getPatient(id=1, dob='2000-6-10'):
    conn = connect(host="127.0.0.1", database="hospital", user="root", password='password')
    curr = conn.cursor()
    query = "select * from hospital.patients where patient_id=%d and dob='%s'"
    param = (id, dob)
    curr.execute(query % param)
    result = curr.fetchone()
    print(result)
    if (result == None):
        return None
    current_patient = Patients(id=result[0], name=result[1], age=result[2], gender=result[3], email=result[4],
                               phone_number=result[5], dob=result[6], image=result[7])
    curr.close()
    conn.close()
    return current_patient


def getEntries(id=1):
    conn = connect(host="127.0.0.1", database="hospital", user="root", password='password')
    curr = conn.cursor()
    query = '''SELECT d.disease_name, count(e.disease_id) as freq
                FROM
                 entries e
                JOIN
                 disease d ON e.disease_id = d.disease_id
                GROUP BY e.disease_id;'''
    param = (id,)
    curr.execute(query)
    result = curr.fetchall()
    print(result)
    curr.close()
    conn.close()
    return result


def insertData(patient):
    conn = connect(host="127.0.0.1", database="hospital", user="root", password='password')
    curr = conn.cursor()
    if patient.image!=None:
        query = "insert into hospital.patients(full_name,age,gender,email,phone_no,dob,image) values('%s',%d,'%s','%s','%s','%s','%s')"
        params = (patient.name, patient.age, patient.gender, patient.email, patient.phone_number, patient.dob, patient.image)
        curr.execute(query % params)
    else:
        query = "insert into hospital.patients(full_name,age,gender,email,phone_no,dob,image) values('%s',%d,'%s','%s','%s','%s')"
        params = (patient.name, patient.age, patient.gender, patient.email, patient.phone_number, patient.dob)
        curr.execute(query % params)

    conn.commit()
    curr.close()
    conn.close()


def execute_query(query, parameters=None):
    conn = connect(host="127.0.0.1", database="hospital", user="root", password='password')
    cur = conn.cursor()
    if (parameters is None):
        cur.execute(query)
    else:
        cur.execute(query%parameters)
    conn.commit()
    cur.close()
    conn.close()

def getRecords(query,params=None):
    conn = connect(host="127.0.0.1", database="hospital", user="root", password='password')
    curr = conn.cursor()
    curr.execute(query % params)
    result = curr.fetchall()
    # print(result)
    curr.close()
    conn.close()
    return result

def insertRecord(params=None):
    conn = connect(host="127.0.0.1", database="hospital", user="root", password='password')
    curr = conn.cursor()
    query="select disease_id from hospital.disease where disease_name='%s'"
    curr.execute(query % params)
    result = curr.fetchone()
    curr.close()
    conn.close()
    return result


if __name__ == '__main__':
    getPatient()