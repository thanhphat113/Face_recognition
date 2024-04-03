import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import DAO.database as db
from DTO.petDTO import pet
import mysql.connector

class petDAO:
    def __init__(self):
        self.pet_list = []
        self.n = 0
        self.conn = db.connect_to_database()
    
    def ReadFromDatabase(self):
        conn = self.conn
        try:
            conn.connect()
            query = "Select * from thunuoi"
            list = db.execute_query(conn, query)
            for item in list:
                tn = pet(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
                self.pet_list.append(tn)
                self.n = self.n + 1
            return self.pet_list
        except mysql.connector.Error as error:
            print(f'Error: {error}')
            return None
    
    def WriteToDatabase(self):
        conn = self.conn
        try:
            conn.connect()
            query = "Delete from thunuoi"
            db.execute_query(conn, query)
            for item in self.pet_list:
                query = f"Insert into thunuoi values ('{item.get_matn()}', '{item.get_tentn()}', '{item.get_maulong()}', '{item.get_cannang()}', '{item.get_loai()}', '{item.get_giong()}', '{item.get_gioitinh()}', '{item.get_kh()})"
                db.insert_data(conn, query)
        except mysql.connector.Error as error:
            print(f'Error: {error}')

    def find(self, noidung : str, tuychon : str):
        conn = self.conn
        try:
            conn.connect()
            if tuychon == "matn":
                query = f"Select * from thunuoi where matn = {noidung}"
            elif tuychon == "tentn":
                query = f"Select * from thunuoi where tentn = {noidung}"
            elif tuychon == "mau":
                query = f"Select * from thunuoi where mau = {noidung}"
            elif tuychon == "loai":
                query = f"Select * from thunuoi where loai = {noidung}"
            elif tuychon == "giong":
                query = f"Select * from thunuoi where giong = {noidung}"
            elif tuychon == "makh":
                query = f"Select * from thunuoi where makh = {noidung}"
            db.execute_query(conn, query)
        except mysql.connector.Error as error:
            print(f'Error: {error}')
        

    def add(self, tn : pet):
        self.pet_list.append(tn)

    def remove(self, tn : pet):
        self.pet_list.remove(tn)

    def edit(self, tn : pet):
        for i in range(self.n):
            if self.pet_list[i].get_matn() == tn.get_matn():
                self.pet_list[i] = tn

if __name__ == "__main__":
    dstn = petDAO()
    qltn = dstn.ReadFromDatabase()
    for tn in qltn:
        print(f"Mã thú nuôi: {tn.get_matn()}, Tên thú nuôi: {tn.get_tentn()}, Màu lông: {tn.get_maulong()}, Cân nặng: {tn.get_cannang()}, Loài: {tn.get_loai()}, Giống: {tn.get_giong()}, Giới tính: {tn.get_gioitinh()}, Khách hàng: {tn.get_kh()}")