import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import DAO.database as db
from DTO.billDTO import bill
import mysql.connector

class billDAO:
    def __init__(self):
        self.bill_list = []
        self.n = 0
        self.conn = db.connect_to_database()
    
    def ReadFromDatabase(self):
        conn = self.conn
        try:
            conn.connect()
            query = "Select * from hoadon"
            list = db.execute_query(conn, query)
            for item in list:
                bll = bill(item[0], item[1], item[2], item[3], item[4])
                self.bill_list.append(bll)
                self.n = self.n + 1
            return self.bill_list
        except mysql.connector.Error as error:
            print(f'Error: {error}')
            return None
    
    def WriteToDatabase(self):
        conn = self.conn
        try:
            conn.connect()
            query = "Delete from hoadon"
            db.execute_query(conn, query)
            for item in self.bill_list:
                query = f"Insert into hoadon values ('{item.get_mahd()}', '{item.get_ngaytao()}', '{item.get_tongtien()}', '{item.get_manv()}', '{item.get_makh()}')"
                db.insert_data(conn, query)
        except mysql.connector.Error as error:
            print(f'Error: {error}')

    def find(self, noidung : str, tuychon : str):
        conn = self.conn
        try:
            conn.connect()
            if tuychon == "mahd":
                query = f"Select * from hoadon where mahd = {noidung}"
            elif tuychon == "ngaytao":
                query = f"Select * from hoadon where ngaytao = {noidung}"
            elif tuychon == "manv":
                query = f"Select * from hoadon where manv = {noidung}"
            elif tuychon == "makh":
                query = f"Select * from hoadon where makh = {noidung}"
            db.execute_query(conn, query)
        except mysql.connector.Error as error:
            print(f'Error: {error}')
        

    def add(self, bll : bill):
        self.bill_list.append(bll)

    def remove(self, bll : bill):
        self.bill_list.remove(bll)

    def edit(self, bll : bill):
        for i in range(self.n):
            if self.bill_list[i].get_mahd() == bll.get_mahd():
                self.bill_list[i] = bll

if __name__ == "__main__":
    dshd = billDAO()
    qlhd = dshd.ReadFromDatabase()
    for bll in qlhd:
        print(f"Mã hóa đơn: {bll.get_mahd()}, Ngày tạo: {bll.get_ngaytao()}, Tổng tiền: {bll.get_tongtien()}, Nhân viên: {bll.get_kh()}, Khách hàng: {bll.get_email()}")