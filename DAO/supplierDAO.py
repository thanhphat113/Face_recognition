import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import DAO.database as db
from DTO.supplierDTO import Supplier
import mysql.connector

class supplierDAO:
    def __init__(self):
        self.conn = db.connect_to_database()
    
    def getAllSuppliers(self):
        supplier_list = []
        conn = self.conn
        try:
            conn.connect()
            query="Select * from nhacungcap"
            list=db.execute_fetch_all(conn,query)
            for ncc in list:
                supplier = Supplier(ncc[0],ncc[1],ncc[2],ncc[3],ncc[4])
                supplier_list.append(supplier)
            return supplier_list
        except mysql.connector.Error as error:
            print(f'Error: {error}')
            return None
        finally:
            conn.close()

    def getSupplierById(self, id):
        conn=self.conn
        try:
            conn.connect()
            query=f"Select * from nhacungcap where mancc = '{id}'"
            result = db.execute_fetch_one(conn,query)
            supplier = Supplier(result[0],result[1],result[2],result[3],result[4])
            return supplier
        except mysql.connector.Error as error:
            return 'Excute thất bại !!!!'
    
    def insert(self, sup : Supplier):
        conn=self.conn
        try:
            conn.connect()
            query=f"insert into nhacungcap(tenncc,email,diachi,sdt) values ('{sup.tenncc}','{sup.email}','{sup.diachi}','{sup.sdt}')"
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
            query=f"delete from nhacungcap where mancc = '{id}'"
            db.execute_query(conn,query)
            return 'Xoá thành công !!!!'
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            conn.close()
            
    def update(self, sup : Supplier):
        conn=self.conn
        try:
            conn.connect()
            query=f"update nhacungcap set tenncc = '{sup.tenncc}', email = '{sup.email}', diachi = '{sup.diachi}', sdt = '{sup.sdt}' where mancc = '{sup.mancc}'"
            db.execute_query(conn,query)
            return 'Cập nhật thành công !!!!'
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            conn.close()

    def findByCondition(self, type, condition):
        Supplier_list = []
        try:
            self.conn.connect()
            query = f"select * from nhacungcap where {type} like '%{condition}%'"
            result = db.execute_fetch_all(self.conn,query)
            if result is not None:
                for ncc in result:
                    sup = Supplier(ncc[0],ncc[1],ncc[2],ncc[3],ncc[4])
                    Supplier_list.append(sup)
            return Supplier_list
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            self.conn.close()