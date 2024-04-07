
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import DAO.database as db
from DTO.phongbenhDTO import phongbenh
import mysql.connector


class phongbenhDAO:
    def __init__(self):
        self.conn = db.connect_to_database()
    
    def find_All(self):
        phongbenh_list=[]
        conn=self.conn
        try:
            conn.connect()
            query="Select * from PhongBenh"
            list=db.execute_fetch_all(conn,query)
            for pb in list:
                emp=phongbenh(pb[0],pb[1],pb[2],pb[3])
                phongbenh_list.append(emp)
            return phongbenh_list
        except mysql.connector.Error as error:
            print(f'Error: {error}')
            return None
        finally:
            conn.close()
    
    def insert(self, emp:phongbenh):
        conn=self.conn
        try:
            conn.connect()
            query=f"insert into phongbenh(tenpb,tinhtrang) values ('{emp.tenpb}','{emp.loaitinhtrang}')"
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
            query=f"delete from PhongBenh where mapb = '{id}'"
            db.execute_query(conn,query)
            return 'Xoá thành công !!!!'
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            conn.close()
            
    def update(self,emp:phongbenh):
        conn=self.conn
        try:
            conn.connect()
            thunuoi = "NULL"
            query=f"update PhongBenh set tenpb = '{emp.tenpb}',tinhtrang = '{emp.loaitinhtrang}', matn = {thunuoi} where mapb = '{emp.mapb}'"
            if emp.matn is not None:
                query=f"update PhongBenh set tenpb = '{emp.tenpb}',tinhtrang = '{emp.loaitinhtrang}', matn = '{emp.matn}' where mapb = '{emp.mapb}'"
            db.execute_query(conn,query)
            return 'Cập nhật thành công !!!!'
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            conn.close()
        
    def findByCondition(self, type, condition):
        phongbenh_list = []
        try:
            self.conn.connect()
            query = f"select * from PhongBenh where {type} like '%{condition}%'"
            if type == "tinhtrang":
                query = f"select * from PhongBenh where {type} = {condition}"
            result = db.execute_fetch_all(self.conn,query)
            if result is not None:
                for nv in result:
                    emp = phongbenh(nv[0],nv[1],nv[2],nv[3])
                    phongbenh_list.append(emp)
            return phongbenh_list
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            self.conn.close()
        
    def findByPetName(self,condition):
        phongbenh_list = []
        try:
            self.conn.connect()
            query = f"SELECT pb.*,tn.tentn FROM `PhongBenh` as pb join ThuNuoi as tn WHERE pb.matn = tn.matn and tn.tentn like '%{condition}%'"
            result = db.execute_fetch_all(self.conn,query)
            if result is not None:
                for nv in result:
                    emp = phongbenh(nv[0],nv[1],nv[2],nv[3])
                    phongbenh_list.append(emp)
            return phongbenh_list
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            self.conn.close()
            
if __name__ == "__main__":
    pbDAO = phongbenhDAO()
    result = pbDAO.findByCondition('tinhtrang',1)
    for pb in result:
        print(pb.mapb)
        