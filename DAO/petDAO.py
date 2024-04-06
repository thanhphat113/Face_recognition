import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import DAO.database as db
from DTO.petDTO import pet
import mysql.connector

class petDAO:
    def __init__(self):
        self.conn = db.connect_to_database()
    
    def ReadFromDatabase(self):
        thunuoi_list=[]
        conn = self.conn
        try:
            conn.connect()
            query = "Select * from ThuNuoi"
            list = db.execute_fetch_all(conn, query)
            for item in list:
                tn = pet(item[0], item[1], item[2], item[3], item[4])
                thunuoi_list.append(tn)
            return thunuoi_list
        except mysql.connector.Error as error:
            print(f'Error: {error}')
            return None
    
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
            db.execute_fetch_all(conn, query)
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
                
    def findById(self,id):
        result = None
        try:
            self.conn.connect()
            query = f"select * from ThuNuoi where matn = '{id}'"
            list = db.execute_fetch_all(self.conn,query)
            for subpet in list:
                result = pet(subpet[0],subpet[1],subpet[2],subpet[3],subpet[4])
            return result
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
    
    def findByName(self,name):
        result = None
        try:
            self.conn.connect()
            query = f"select * from ThuNuoi where tentn = '{name}'"
            list = db.execute_fetch_all(self.conn,query)
            for subpet in list:
                result = pet(subpet[0],subpet[1],subpet[2],subpet[3],subpet[4])
            return result
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
    
    def findPetDontUseBed(self):
        pet_list = []
        try:
            self.conn.connect()
            query = 'SELECT ThuNuoi.* FROM ThuNuoi LEFT JOIN PhongBenh ON PhongBenh.matn = ThuNuoi.matn WHERE PhongBenh.matn IS NULL'
            result = db.execute_fetch_all(self.conn,query)
            for subpet in result:
                tn = pet(subpet[0],subpet[1],subpet[2],subpet[3],subpet[4])
                pet_list.append(tn)
            return pet_list
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        
if __name__ == "__main__":
    pets = petDAO()
    result = pets.findById(1)
    print(f"{result.get_tentn()}")

