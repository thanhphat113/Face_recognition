
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import DAO.database as db
from DTO.loaitaikhoanDTO import loaitaikhoan
import mysql.connector

class loaiDAO:
    def __init__(self):
        self.conn = db.connect_to_database()
        
    def findById(self,id : loai.maLoai):
        try:
            self.conn.connect()
            query = f"select * from LoaiTaiKhoan where maloai = '{id}'"
            loaitk = db.execute_fetch_one(self.conn,query)
            return loaitk
        except mysql.connector.Error as error:
            return f'Error: {error}'
        finally:
            self.conn.close()
            