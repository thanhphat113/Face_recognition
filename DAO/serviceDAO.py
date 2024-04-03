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
                service = Service(dv[0],dv[1],dv[2],dv[3])
                service_list.append(service)
            return service_list
        except mysql.connector.Error as error:
            print(f'Error: {error}')
            return None
        finally:
            conn.close()
    
    def insertService(self, service):
        conn=self.conn
        try:
            conn.connect()
            query=f"insert into dichvu(tendv, giatien, maloaidv) values ('{service.getTen()}', '{service.getGia()}', '{service.getMaLoaiDV()}')"
            db.execute_query(conn,query)
            return 'Thêm thành công !!!!'
        except mysql.connector.Error as error:
            return 'Thêm thất bại !!!!'
        