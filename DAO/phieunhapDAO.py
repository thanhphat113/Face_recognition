import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import DAO.database as db
from DTO.phieunhapDTO import PhieuNhap 
import mysql.connector

class phieunhapDAO:
    def __init__(self):
        self.conn = db.connect_to_database()

    def getAllPhieuNhap(self):
        pn_list = []
        conn = self.conn
        try:
            conn.connect()
            query="select * from phieunhap"
            list=db.execute_fetch_all(conn,query)
            for pn in list:
                phieunhap = PhieuNhap(pn[0],pn[1],pn[2],pn[3],pn[4])
                pn_list.append(phieunhap)
            return pn_list
        except mysql.connector.Error as error:
            print(f'Error: {error}')
            return None
        finally:
            conn.close()
    
    def insertPhieuNhap(self, pn):
        conn=self.conn
        try:
            conn.connect()
            query=f"insert into phieunhap(manv, mancc, ngaytao, tongtien) values ('{pn.getMaNV()}', '{pn.getMaNCC()}', '{pn.getNgayTao()}', '{pn.getTongTien()}')"
            db.execute_query(conn,query)
            return 'Thêm thành công !!!!'
        except mysql.connector.Error as error:
            return 'Thêm thất bại !!!!'
        finally:
            conn.close()
        
    def updateTotalPrice(self, mapn, totalprice):
        conn = self.conn
        try:
            conn.connect()
            query=f"update phieunhap set tongtien = '{totalprice}' where mapn = '{mapn}'"
            db.execute_query(conn, query)
            return "Sửa thành công!"
        except mysql.connector.Error as error:
            return "Sửa thất bại!"

    def updatePhieuNhap(self, pn):
        conn = self.conn
        try:
            conn.connect()
            query=f"update phieunhap set manv = '{pn.getMaNV()}', mancc = '{pn.getMaNCC()}', ngaytao = STR_TO_DATE('{pn.getNgayTao()}', '%m-%d-%Y'), tongtien = '{pn.getTongTien()}' where mapn = '{pn.getMaPN()}'"
            db.execute_query(conn, query)
            return "Sửa thành công!"
        except mysql.connector.Error as error:
            return "Sửa thất bại!"
        
    def deletePhieuNhap(self, mapn):
        conn = self.conn
        try:
            conn.connect()
            query=f"delete from chitiet_pn where mapn = '{mapn}'"
            db.execute_query(conn, query)
            query=f"delete from phieunhap where mapn = '{mapn}'"
            db.execute_query(conn, query)
            return "Xóa thành công!"
        except mysql.connector.Error as error:
            return "Xóa thất bại!"
        
    def searchPhieuNhap(self, search, choice):
        pn_list = []
        conn = self.conn
        try:
            conn.connect()
            if choice == 0:
                query=f"select * from phieunhap where mapn LIKE '{search}%'"
            elif choice == 1:
                query=f"select * from phieunhap where manv LIKE '{search}%'"
            elif choice == 2:
                query=f"select * from phieunhap where mancc LIKE '{search}%'"

            list=db.execute_fetch_all(conn,query)
            for pn in list:
                phieunhap = PhieuNhap(pn[0],pn[1],pn[2],pn[3],pn[4])
                pn_list.append(phieunhap)
            return pn_list
        except mysql.connector.Error as error:
            print(f'Error: {error}')
            return None
        finally:
            conn.close()
    