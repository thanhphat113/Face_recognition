import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import DAO.database as db
from DTO.service_categoryDTO import ServiceCategory 
import mysql.connector

class serviceCategoryDAO:
    def __init__(self):
        self.conn = db.connect_to_database()

    def getAllServiceCategories(self):
        service_category_list = []
        conn = self.conn
        try:
            conn.connect()
            query="Select * from loaidv"
            list=db.execute_fetch_all(conn,query)
            for loaidv in list:
                service = ServiceCategory(loaidv[0],loaidv[1])
                service_category_list.append(service)
            return service_category_list
        except mysql.connector.Error as error:
            print(f'Error: {error}')
            return None
        finally:
            conn.close()
    
    def insertServiceCategory(self, service_category):
        conn=self.conn
        try:
            conn.connect()
            query=f"insert into loaidv(tenloai) values ('{service_category.getTenLoai()}')"
            db.execute_query(conn,query)
            return 'Thêm thành công !!!!'
        except mysql.connector.Error as error:
            return 'Thêm thất bại !!!!'
        
    def updateServiceCategory(self, service_category):
        conn=self.conn
        try:
            conn.connect()
            query=f"UPDATE loaidv SET tenloai = '{service_category.getTenLoai()}' WHERE maloaidv = '{service_category.getMaLoaiDV()}'"
            db.execute_query(conn,query)
            return 'Sửa thành công !!!!'
        except mysql.connector.Error as error:
            return 'Sửa thất bại !!!!'
        
    def deleteServiceCategory(self, service_category_id):
        conn=self.conn
        try:
            conn.connect()
            query=f"DELETE FROM loaidv WHERE maloaidv = '{service_category_id}'"
            db.execute_query(conn,query)
            return 'Xóa thành công !!!!'
        except mysql.connector.Error as error:
            return 'Xóa thất bại !!!!'