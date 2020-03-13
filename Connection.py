from pymysql import *


def get_data():
    conn = connect(host="127.0.0.1", database="hospital", user="root", password='password')
    print("connected")
    curr = conn.cursor()
    query = "select * from hospital.patients"
    curr.execute(query)
    result = curr.fetchone()
    print(result)
    curr.close()
    conn.close()


get_data()
