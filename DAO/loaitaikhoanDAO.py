import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import DAO.database as db
from DTO.loaitaikhoanDTO import loaitaikhoan

class loaitaikhoanDAO:
    def __init__(self):
        self.conn = db.connect_to_database()


    def find_All(self):
        loaitaikhoan_list=[]
        conn = self.conn
        try:
            conn.connect()
            query = "Select * from LoaiTaiKhoan"
            list = db.execute_fetch_all(conn, query)
            for item in list:
                accountType = loaitaikhoan(item[0], item[1])
                loaitaikhoan_list.append(accountType)
            return loaitaikhoan_list
        except mysql.connector.Error as error:
            print(f'Error: {error}')
            return None
    
    def findById(self,id):
        try:
            self.conn.connect()
            query = f"select * from LoaiTaiKhoan where maloai = '{id}'"
            loaitk = db.execute_fetch_one(self.conn,query)
            return loaitk
        except mysql.connector.Error as error:
            return f'Error: {error}'
        finally:
            self.conn.close()