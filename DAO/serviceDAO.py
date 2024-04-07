import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import DAO.database as db
from DTO.serviceDTO import Service 
import mysql.connector

class serviceDAO:
    def __init__(self):
        self.conn = db.connect_to_database()

    def getAllServices(self):
        service_list = []
        conn = self.conn
        try:
            conn.connect()
            query="Select * from dichvu"
            list=db.execute_fetch_all(conn,query)
            for dv in list:
                service = Service(dv[0],dv[1],dv[2])
                service_list.append(service)
            return service_list
        except mysql.connector.Error as error:
            print(f'Error: {error}')
            return None
        finally:
            conn.close()
    
    def getServiceById(self, id):
        conn=self.conn
        try:
            conn.connect()
            query=f"Select * from dichvu where madv = '{id}'"
            result = db.execute_fetch_one(conn,query)
            service = Service(result[0],result[1],result[2])
            return service
        except mysql.connector.Error as error:
            return 'Excute thất bại !!!!'
        
    def insertService(self, service):
        conn=self.conn
        try:
            conn.connect()
            query=f"insert into dichvu(tendv, giatien) values ('{service.getTen()}', '{service.getGia()}')"
            db.execute_query(conn,query)
            return 'Thêm thành công !!!!'
        except mysql.connector.Error as error:
            return 'Thêm thất bại !!!!'
        
    def updateService(self, service):
        conn = self.conn
        try:
            conn.connect()
            query=f"update dichvu set tendv = '{service.getTen()}',giatien = '{service.getGia()}' where madv = '{service.getMaDV()}'"
            db.execute_query(conn, query)
            return "Sửa thành công!"
        except mysql.connector.Error as error:
            return "Sửa thất bại!"
        
    def deleteService(self, madv):
        conn = self.conn
        try:
            conn.connect()
            query=f"delete from dichvu where madv = '{madv}'"
            db.execute_query(conn, query)
            return "Xóa thành công!"
        except mysql.connector.Error as error:
            return "Xóa thất bại!"
        
    def searchService(self, search, choice):
        service_list = []
        conn = self.conn
        try:
            conn.connect()
            if choice == 0:
                query=f"select * from dichvu where madv LIKE '%{search}%'"
            elif choice == 1:
                query=f"select * from dichvu where tendv LIKE '%{search}%'"

            list=db.execute_fetch_all(conn,query)
            for dv in list:
                service = Service(dv[0],dv[1],dv[2])
                service_list.append(service)
            return service_list
        except mysql.connector.Error as error:
            print(f'Error: {error}')
            return None
        finally:
            conn.close()
    