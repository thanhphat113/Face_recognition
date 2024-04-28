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
            query=f"insert into hoadon(ngaytao, tongtien, manv, makh) values ('{bill.get_ngaytao()}','{bill.get_tongtien()}','{bill.get_manv()}','{bill.get_makh()}')"
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
            query=f"delete from chitiet_hd where mahd = '{id}'"
            db.execute_query(conn, query)
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
            query=f"update hoadon set ngaytao = STR_TO_DATE('{bill.get_ngaytao()}', '%m-%d-%Y'), tongtien = '{bill.get_tongtien()}', manv = '{bill.get_manv()}', makh = '{bill.get_makh()}' where mahd = '{bill.get_mahd()}'"
            db.execute_query(conn, query)
            return 'Cập nhật thành công !!!!'
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            conn.close()

    def updateTotalPrice(self, mahd, totalprice):
        conn = self.conn
        try:
            conn.connect()
            query=f"update hoadon set tongtien = '{totalprice}' where mahd = '{mahd}'"
            db.execute_query(conn, query)
            return "Sửa thành công!"
        except mysql.connector.Error as error:
            return "Sửa thất bại!"
        
    def updateTotalPrice2(self, totalprice):
        conn = self.conn
        try:
            conn.connect()
            query=f"update hoadon set tongtien = tongtien +'{totalprice}' where mahd = (SELECT MAX(mahd) FROM hoadon)"
            db.execute_query(conn, query)
            return "Sửa thành công!"
        except mysql.connector.Error as error:
            return "Sửa thất bại!"
    
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
        
    def searchHoaDon(self, search, choice):
        hd_list = []
        conn = self.conn
        try:
            conn.connect()
            if choice == 0:
                query=f"select * from hoadon where mahd LIKE '{search}%'"
            elif choice == 1:
                query=f"select * from hoadon where manv LIKE '{search}%'"
            elif choice == 2:
                query=f"select * from hoadon where makh LIKE '{search}%'"

            list=db.execute_fetch_all(conn,query)
            for hd in list:
                hoadon = bill(hd[0],hd[1],hd[2],hd[3],hd[4])
                hd_list.append(hoadon)
            return hd_list
        except mysql.connector.Error as error:
            print(f'Error: {error}')
            return None
        finally:
            conn.close()