import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import DAO.database as db
from DTO.ctpnDTO import CTPN 
import mysql.connector

class ctpnDAO:
    def __init__(self):
        self.conn = db.connect_to_database()

    def getCTPNById(self, mapn):
        ctpn_list = []
        conn = self.conn
        try:
            conn.connect()
            query=f"select * from chitiet_pn where mapn = {mapn}"
            list=db.execute_fetch_all(conn,query)
            for ct in list:
                ctpn = CTPN(ct[0],ct[1],ct[2],ct[3],ct[4])
                ctpn_list.append(ctpn)
            return ctpn_list
        except mysql.connector.Error as error:
            print(f'Error: {error}')
            return None
        finally:
            conn.close()
    
    def insertCTPN(self, ctpn):
        conn=self.conn
        try:
            conn.connect()
            query=f"insert into chitiet_pn(mapn, madp, soluong, gia, thanhtien) values ('{ctpn.getMaPN()}', '{ctpn.getMaDP()}', '{ctpn.getSoLuong()}', '{ctpn.getGia()}', '{ctpn.getThanhTien()}')"
            db.execute_query(conn,query)
            return 'Thêm thành công !!!!'
        except mysql.connector.Error as error:
            return 'Thêm thất bại !!!!'
        
    def updateCTPN(self, ctpn):
        conn = self.conn
        try:
            conn.connect()
            query=f"update chitiet_pn set madp = '{ctpn.getMaDP()}', soluong = {ctpn.getSoLuong()}, gia = '{ctpn.getGia()}', thanhtien = '{ctpn.getThanhTien()}' where mapn = '{ctpn.getMaPN()}'"
            db.execute_query(conn, query)
            return "Sửa thành công!"
        except mysql.connector.Error as error:
            return "Sửa thất bại!"
        
    def deleteCTPN(self, mapn, madp):
        conn = self.conn
        try:
            conn.connect()
            query=f"delete from chitiet_pn where mapn = '{mapn}' and madp = '{madp}'"
            db.execute_query(conn, query)
            return "Xóa thành công!"
        except mysql.connector.Error as error:
            return "Xóa thất bại!"

    