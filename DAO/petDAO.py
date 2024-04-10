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
    
    def insert(self, pet : pet):
        conn = self.conn
        try:
            conn.connect()
            query=f"insert into thunuoi(tentn, mau, cannang, makh) values ('{pet.get_tentn()}','{pet.get_maulong()}','{pet.get_cannang()}','{pet.get_makh()}')"
            db.execute_query(conn,query)
            return 'Thêm thành công !!!!'
        except mysql.connector.Error as error:
            return 'Thêm thất bại !!!!'
        finally:
            conn.close()

    def findById1(self,id):
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
        finally:
            self.conn.close()

    def delete(self, id):
        conn = self.conn
        try:
            conn.connect()
            query=f"delete from thunuoi where matn = '{id}'"
            db.execute_query(conn,query)
            return 'Xoá thành công !!!!'
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            conn.close()

    def update(self, pet : pet):
        conn = self.conn
        try:
            conn.connect()
            query=f"update thunuoi set tentn = '{pet.get_tentn()}', mau = '{pet.get_maulong()}', cannang = '{pet.get_cannang()}', makh = '{pet.get_makh()}' where matn = '{pet.get_matn()}'"
            db.execute_query(conn,query)
            return 'Cập nhật thành công !!!!'
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            conn.close()
                
    def findById(self,id):
        pets_list = []
        try:
            self.conn.connect()
            query = f"select * from ThuNuoi where matn = '{id}'"
            list = db.execute_fetch_all(self.conn,query)
            if list is not None:
                for subpet in list:
                    result = pet(subpet[0],subpet[1],subpet[2],subpet[3],subpet[4])
                    pets_list.append(result)
            return pets_list
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            self.conn.close()
     
        
    def findByName(self,name):
        pets_list = []
        try:
            self.conn.connect()
            query = f"select * from ThuNuoi where tentn like '%{name}%'"
            list = db.execute_fetch_all(self.conn,query)
            if list is not None:
                for subpet in list:
                    result = pet(subpet[0],subpet[1],subpet[2],subpet[3],subpet[4])
                    pets_list.append(result)
            return pets_list
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            self.conn.close()
        

    def findByColor(self,color):
        pets_list = []
        try:
            self.conn.connect()
            query = f"select * from ThuNuoi where mau = '{color}'"
            list = db.execute_fetch_all(self.conn,query)
            if list is not None:
                for subpet in list:
                    result = pet(subpet[0],subpet[1],subpet[2],subpet[3],subpet[4])
                    pets_list.append(result)
            return pets_list
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            self.conn.close()
    

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
        finally:
            self.conn.close()
        
        
if __name__ == "__main__":
    pets = petDAO()
    result = pets.findById(1)
    print(f"{result.get_tentn()}")

