
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import DAO.database as db
from DTO.employeeDTO import employee 
import mysql.connector


class employeeDAO:
    def __init__(self):
        self.conn = db.connect_to_database()
    
    def find_All(self):
        employee_list=[]
        conn=self.conn
        try:
            conn.connect()
            query="Select * from NhanVien"
            list=db.execute_query(conn,query)
            for nv in list:
                emp=employee(nv[0],nv[1],nv[2],nv[3])
                employee_list.append(emp)
            return employee_list
        except mysql.connector.Error as error:
            print(f'Error: {error}')
            return None
    
if __name__=="__main__":
    emDAO= employeeDAO()
    employees = emDAO.find_All()
    for nv in employees:
        print(f'Mã nhân viên: {nv.manv}, Tên nhân viên: {nv.tennv}, Email: {nv.email}, Số điện thoại: {nv.sdt}')
