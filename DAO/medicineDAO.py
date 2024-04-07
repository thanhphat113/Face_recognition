import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import DAO.database as db
from DTO.medicineDTO import Medicine 
import mysql.connector

class medicineDAO:
    def __init__(self):
        self.conn = db.connect_to_database()

    def getAllMedicines(self):
        medicine_list = []
        conn = self.conn
        try:
            conn.connect()
            query="Select * from duocpham"
            list=db.execute_fetch_all(conn,query)
            for dp in list:
                medicine = Medicine(dp[0],dp[1],dp[2],dp[3],dp[4],dp[5])
                medicine_list.append(medicine)
            return medicine_list
        except mysql.connector.Error as error:
            print(f'Error: {error}')
            return None
        finally:
            conn.close()

    def getMedicineById(self, id):
        conn=self.conn
        try:
            conn.connect()
            query=f"Select * from duocpham where madp = '{id}'"
            result = db.execute_fetch_one(conn,query)
            medicine = Medicine(result[0],result[1],result[2],result[3],result[4],result[5])
            return medicine
        except mysql.connector.Error as error:
            return 'Excute thất bại !!!!'
    
    def insertMedicine(self, medicine):
        conn=self.conn
        try:
            conn.connect()
            query=f"insert into duocpham(tendp, ngaysanxuat, ngayhethan, soluong, giathanh) values ('{medicine.getTenDP()}', STR_TO_DATE('{medicine.getNSX()}', '%m-%d-%Y'), STR_TO_DATE('{medicine.getHSD()}', '%m-%d-%Y'), '{medicine.getSoLuong()}', '{medicine.getGia()}')"
            db.execute_query(conn,query)
            return 'Thêm thành công !!!!'
        except mysql.connector.Error as error:
            return 'Thêm thất bại !!!!'
        
    def updateMedicine(self, medicine):
        conn = self.conn
        try:
            conn.connect()
            query=f"update duocpham set tendp = '{medicine.getTenDP()}', ngaysanxuat = STR_TO_DATE('{medicine.getNSX()}', '%m-%d-%Y'), ngayhethan = STR_TO_DATE('{medicine.getHSD()}', '%m-%d-%Y'), soluong = '{medicine.getSoLuong()}', giathanh = '{medicine.getGia()}' where madp = '{medicine.getMaDP()}'"
            db.execute_query(conn, query)
            return "Sửa thành công!"
        except mysql.connector.Error as error:
            return "Sửa thất bại!"
        
    def deleteMedicine(self, madp):
        conn = self.conn
        try:
            conn.connect()
            query=f"delete from duocpham where madp = '{madp}'"
            db.execute_query(conn, query)
            return "Xóa thành công!"
        except mysql.connector.Error as error:
            return "Xóa thất bại!"
        
    def searchMedicine(self, search, choice):
        medicine_list = []
        conn = self.conn
        try:
            conn.connect()
            if choice == 0:
                query=f"select * from duocpham where madp LIKE '{search}%'"
            elif choice == 1:
                query=f"select * from duocpham where tendp LIKE '{search}%'"

            list=db.execute_fetch_all(conn,query)
            for dp in list:
                medicine = Medicine(dp[0],dp[1],dp[2],dp[3],dp[4],dp[5])
                medicine_list.append(medicine)
            return medicine_list
        except mysql.connector.Error as error:
            print(f'Error: {error}')
            return None
        finally:
            conn.close()
    