from pymysql import *
from patients import *
from DoctorClass import *

# creates patient object
def getPatientbyId(id=1, dob='2000-6-10'):
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

#Creates patient 2 for signup to patient_info directly:
def getPatientbyName(name='paras_gurnani', dob='2000-06-10'):
    conn = connect(host="127.0.0.1", database="hospital", user="root", password='password')
    curr = conn.cursor()
    query = "select * from hospital.patients where full_name='%s' and dob='%s'"
    param = (name, dob)
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

# used in piechart plotting
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

# to add new patient
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

# for record table
def getRecords(query,params=None):
    conn = connect(host="127.0.0.1", database="hospital", user="root", password='password')
    curr = conn.cursor()
    curr.execute(query % params)
    result = curr.fetchall()
    # print(result)
    curr.close()
    conn.close()
    return result

# new disease
def insertRecord(params=None):
    conn = connect(host="127.0.0.1", database="hospital", user="root", password='password')
    curr = conn.cursor()
    query="select disease_id from hospital.disease where disease_name='%s'"
    curr.execute(query % params)
    result = curr.fetchone()
    curr.close()
    conn.close()
    return result

def getDoctor(id=1, pas='alpha'):
    conn = connect(host='127.0.0.1', database='hospital', user='root', password='password')
    curr = conn.cursor()
    query = "SELECT * FROM doctors WHERE doctor_id=%d AND password='%s'"
    param = (id,pas)
    curr.execute(query % param)
    result = curr.fetchone()
    if result!=None:
        newDoctor = Doctor(result[0],result[2])
    else:
        newDoctor = None
    curr.close()
    conn.close()
    return newDoctor


def analysePatients(param):
    conn = connect(host="127.0.0.1", database="hospital", user="root", password='password')
    curr = conn.cursor()
    query = '''SELECT 
                    MONTHNAME(date_of_entry),count((monthname(date_of_entry)))
                FROM
                    entries
                where
	                monthname(date_of_entry)='%s';'''
    curr.execute(query%param)
    result = curr.fetchall()
    # print(result)
    curr.close()
    conn.close()
    return result


def updateDoctor(dr):
    conn = connect(host='127.0.0.1', database='hospital', user='root', password='password')
    curr = conn.cursor()
    query = ''' UPDATE doctors
                SET patient_list = '%s' WHERE doctor_id = %d'''

    print('In connection: ',dr.patients, dr.id)
    # x=input('Enter num = ') for debugging
    param = (str(dr.patients), int(dr.id))

    curr.execute(query % param)
    #Forget to add conn.commit()
    conn.commit()
    curr.close()
    conn.close()

