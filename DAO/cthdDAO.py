import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import DAO.database as db
from DTO.cthdDTO import CTHD 
import mysql.connector

class cthdDAO:
    def __init__(self):
        self.conn = db.connect_to_database()

    def getCTHDById(self, mahd):
        cthd_list = []
        conn = self.conn
        try:
            conn.connect()
            query = f"select * from chitiet_hd where mahd = {mahd}"
            list = db.execute_fetch_all(conn,query)
            for ct in list:
                cthd = CTHD(ct[0], ct[1], ct[2], ct[3])
                cthd_list.append(cthd)
            return cthd_list
        except mysql.connector.Error as error:
            print(f'Error: {error}')
            return None
        finally:
            conn.close()
    
    def insertCTHD(self, cthd):
        conn = self.conn
        try:
            conn.connect()
            query = f"insert into chitiet_hd(mahd, madv, soluong, gia) values ('{cthd.get_mahd()}', '{cthd.get_madv()}', '{cthd.get_soLuong()}', '{cthd.get_gia()}')"
            db.execute_query(conn,query)
            return 'Thêm thành công !!!!'
        except mysql.connector.Error as error:
            return 'Thêm thất bại !!!!'
        finally:
            conn.close()
        
    def updateCTHD(self, cthd):
        conn = self.conn
        try:
            conn.connect()
            query=f"update chitiet_pn set madv = '{cthd.get_madv()}', soluong = {cthd.get_soLuong()} where madp = '{cthd.get_gia()}'"
            db.execute_query(conn, query)
            return "Sửa thành công!"
        except mysql.connector.Error as error:
            return "Sửa thất bại!"
        finally:
            conn.close()
