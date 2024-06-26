from unidecode import unidecode
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
            query="Select * from nhanvien"
            list=db.execute_fetch_all(conn,query)
            for nv in list:
                emp=employee(nv[0],nv[1],nv[2],nv[3])
                employee_list.append(emp)
            return employee_list
        except mysql.connector.Error:
            return None
        finally:
            conn.close()

    def getEmployeeById(self, id):
        conn=self.conn
        try:
            conn.connect()
            query=f"Select * from nhanvien where manv = '{id}'"
            result = db.execute_fetch_one(conn,query)
            emp = employee(result[0],result[1],result[2],result[3])
            return emp
        except mysql.connector.Error as error:
            return 'Excute thất bại !!!!'
    
    def insert(self, emp:employee):
        conn = self.conn
        try:
            cursor = conn.cursor()
            query=f"insert into nhanvien(tennv,sdt,email) values ('{emp.tennv}','{emp.sdt}','{emp.email}')"
            cursor.execute(query)
            manv = cursor.lastrowid
            print(manv)
            user = unidecode(emp.tennv).lower().replace(" ", "")
            query_tk = "INSERT INTO taikhoan (username, password, trangthai, maloai, manv) VALUES (%s, %s, %s, %s, %s)"
            values_tk = (user, '123', 1, 2, manv)
            cursor.execute(query_tk,values_tk)
            conn.commit()
            return 'Thêm thành công !!!!'
        except mysql.connector.Error as error:
            return f'Thêm thất bại: {error.msg}'
        finally:
            cursor.close()
        
    def delete(self,id):
        conn=self.conn
        try:
            conn.connect()
            query_tk = f"delete from TaiKhoan where manv = {id}"
            db.execute_query(conn,query_tk)
            query=f"delete from NhanVien where manv = '{id}'"
            db.execute_query(conn,query)
            return 'Xoá thành công !!!!'
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            conn.close()
            
    def update(self,emp:employee):
        conn=self.conn
        try:
            conn.connect()
            query=f"update NhanVien set tennv = '{emp.tennv}',sdt = '{emp.sdt}', email = '{emp.email}' where manv = '{emp.manv}'"
            db.execute_query(conn,query)
            return 'Cập nhật thành công !!!!'
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            conn.close()

    def findByCondition(self, type, condition):
                employee_list = []
                try:
                        self.conn.connect()
                        query = f"select * from NhanVien where {type} like '%{condition}%'"
                        result = db.execute_fetch_all(self.conn,query)
                        if result is not None:
                                for nv in result:
                                        emp = employee(nv[0],nv[1],nv[2],nv[3])
                                        employee_list.append(emp)
                        return employee_list
                except mysql.connector.Error as error:
                        return f'Lỗi: {error}'
                finally:
                        self.conn.close()
                        
    def findByMatk(self, condition):
                emp = None
                try:
                        self.conn.connect()
                        query = f"select * from NhanVien where matk = '{condition}'"
                        result = db.execute_fetch_one(self.conn,query)
                        if result is not None:
                                emp = employee(result[0], result[1], result[2], result[3])
                        return emp
                except mysql.connector.Error as error:
                        return f'Lỗi: {error}'
                finally:
                        self.conn.close()

from DAO.taikhoanDAO import taikhoanDAO
from DTO.taikhoanDTO import taikhoan