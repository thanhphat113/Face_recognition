import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import DAO.database as db
from DTO.billDTO import bill
import mysql.connector

class billDAO:
    def __init__(self):
        self.conn = db.connect_to_database()
    
    def ReadFromDatabase(self):
        bill_list = []
        conn = self.conn
        try:
            conn.connect()
            query = "Select * from hoadon"
            list = db.execute_fetch_all(conn, query)
            for hd in list:
                subBill = bill(hd[0], hd[1], hd[2], hd[3], hd[4])
                bill_list.append(subBill)
            return bill_list
        except mysql.connector.Error as error:
            print(f'Error: {error}')
            return None
        finally:
            conn.close()
    


    def insert(self, bill : bill):
        conn = self.conn
        try:
            conn.connect()
            query=f"insert into hoadon(ngaytao, tongtien) values ('{bill.get_ngaytao()}','{bill.get_tongtien()}')"
            db.execute_query(conn,query)
            return 'Thêm thành công !!!!'
        except mysql.connector.Error as error:
            return 'Thêm thất bại !!!!'
        finally:
            conn.close()

    def delete(self, id):
        conn = self.conn
        try:
            conn.connect()
            query=f"delete from hoadon where mahd = '{id}'"
            db.execute_query(conn,query)
            return 'Xoá thành công !!!!'
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            conn.close()

    def update(self, bill : bill):
        conn = self.conn
        try:
            conn.connect()
            query=f"update hoadon set ngaytao = '{bill.get_ngaytao()}', tongtien = '{bill.get_tongtien()}' where mahd = '{bill.get_mahd()}'"
            db.execute_query(conn, query)
            return 'Cập nhật thành công !!!!'
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            conn.close()

    
    def findById(self, id):
        result = None
        conn = self.conn
        try:
            conn.connect()
            query = f"select * from hoadon where mahd = '{id}'"
            list = db.execute_fetch_all(conn, query)
            for subBill in list:
                result = bill(subBill[0], subBill[1], subBill[2], subBill[3], subBill[4])
            return result
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'