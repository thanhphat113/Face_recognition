import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import DAO.database as db
from DTO.customerDTO import customer
import mysql.connector

class customerDAO:
    def __init__(self):
        self.conn = db.connect_to_database()
    
    def ReadFromDatabase(self):
        cus_list = []
        try:
            self.conn.connect()
            query = "Select * from khachhang"
            list = db.execute_fetch_all(self.conn, query)
            for item in list:
                cus = customer(item[0], item[1], item[2], item[3], item[4])
                cus_list.append(cus)
            return cus_list
        except mysql.connector.Error as error:
            print(f'Error: {error}')
            return None        

    def insert(self, cus:customer):
        conn=self.conn
        try:
            conn.connect()
            query=f"insert into KhachHang(tenkh,gioitinh,sdt,email) values ('{cus.get_tenkh()}','{cus.get_loaigt()}','{cus.get_sdt()}','{cus.get_email()}')"
            db.execute_query(conn,query)
            return 'Thêm thành công !!!!'
        except mysql.connector.Error as error:
            return 'Thêm thất bại !!!!'
        finally:
            conn.close()

    def delete(self,id):
        conn=self.conn
        try:
            conn.connect()
            query=f"delete from KhachHang where makh = '{id}'"
            db.execute_query(conn,query)
            query=f"delete from ThuNuoi where makh = '{id}'"
            db.execute_query(conn,query)
            return 'Xoá thành công !!!!'
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            conn.close()

    def update(self,cus:customer):
        conn=self.conn
        try:
            conn.connect()
            query=f"update KhachHang set tenkh = '{cus.get_tenkh}',sdt = '{cus.get_sdt}', email = '{cus.get_email}', gioitinh = '{cus.get_gioitinh}' where manv = '{cus.get_makh}'"
            db.execute_query(conn,query)
            return 'Cập nhật thành công !!!!'
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            conn.close()
                
    def findByid(self,id):
        cus = None
        try:
            self.conn.connect()
            query = f"select * from KhachHang where makh = '{id}'"
            result = db.execute_fetch_all(self.conn,query)
            for kh in result:
                cus = customer(kh[0],kh[1],kh[2],kh[3],kh[4])
            return cus
        except mysql.connector.Error as error:
            return f'Error: {error}'
        
    def findByName(self,name):
        cus = None
        try:
            self.conn.connect()
            query = f"select * from KhachHang where tenkh = '{name}'"
            result = db.execute_fetch_all(self.conn,query)
            for kh in result:
                cus = customer(kh[0],kh[1],kh[2],kh[3],kh[4])
            return cus
        except mysql.connector.Error as error:
            return f'Error: {error}'
    
    def findByCondition(self, type, condition):
                cus_list = []
                try:
                        self.conn.connect()
                        query = f"select * from KhachHang where {type} like '%{condition}%'"
                        result = db.execute_fetch_all(self.conn,query)
                        if result is not None:
                                for kh in result:
                                        emp = customer(kh[0],kh[1],kh[2],kh[3],kh[4])
                                        cus_list.append(emp)
                        return cus_list
                except mysql.connector.Error as error:
                        return f'Lỗi: {error}'
                finally:
                        self.conn.close()
