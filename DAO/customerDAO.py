import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import DAO.database as db
from DTO.customerDTO import customer
import mysql.connector

class customerDAO:
    def __init__(self):
        self.customer_list = []
        self.n = 0
        self.conn = db.connect_to_database()
    
    def ReadFromDatabase(self):
        conn = self.conn
        try:
            conn.connect()
            query = "Select * from khachhang"
            list = db.execute_fetch_all(conn, query)
            for item in list:
                cus = customer(item[0], item[1], item[2], item[3], item[4])
                self.customer_list.append(cus)
                self.n = self.n + 1
            return self.customer_list
        except mysql.connector.Error as error:
            print(f'Error: {error}')
            return None
    
    def WriteToDatabase(self):
        conn = self.conn
        try:
            conn.connect()
            query = "Delete from khachhang"
            db.execute_fetch_all(conn, query)
            for item in self.customer_list:
                query = f"Insert into khachhang values ('{item.get_makh()}', '{item.get_tenkh()}', '{item.get_gioitinh()}', '{item.get_sdt()}', '{item.get_email()}')"
                db.execute_query(conn, query)
        except mysql.connector.Error as error:
            print(f'Error: {error}')

    def find(self, noidung : str, tuychon : str):
        conn = self.conn
        try:
            conn.connect()
            if tuychon == "makh":
                query = f"Select * from khachhang where makh = {noidung}"
            elif tuychon == "tenkh":
                query = f"Select * from khachhang where tenkh = {noidung}"
            elif tuychon == "sdt":
                query = f"Select * from khachhang where sdt = {noidung}"
            elif tuychon == "email":
                query = f"Select * from khachhang where email = {noidung}"
            db.execute_fetch_all(conn, query)
        except mysql.connector.Error as error:
            print(f'Error: {error}')
        

    def add(self, cus : customer):
        self.customer_list.append(cus)

    def remove(self, cus : customer):
        self.customer_list.remove(cus)

    def edit(self, cus : customer):
        for i in range(self.n):
            if self.customer_list[i].get_makh() == cus.get_makh():
                self.customer_list[i] = cus
                
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
            
