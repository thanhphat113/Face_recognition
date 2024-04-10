import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import DAO.database as db
from DTO.supplierDTO import Supplier
import mysql.connector

class supplierDAO:
    def __init__(self):
        self.conn = db.connect_to_database()

    def getAllSuppliers(self):
        supplier_list = []
        conn = self.conn
        try:
            conn.connect()
            query="Select * from nhacungcap"
            list=db.execute_fetch_all(conn,query)
            for ncc in list:
                supplier = Supplier(ncc[0],ncc[1],ncc[2],ncc[3],ncc[4])
                supplier_list.append(supplier)
            return supplier_list
        except mysql.connector.Error as error:
            print(f'Error: {error}')
            return None
        finally:
            conn.close()

    def getSupplierById(self, id):
        conn=self.conn
        try:
            conn.connect()
            query=f"Select * from nhacungcap where mancc = '{id}'"
            result = db.execute_fetch_one(conn,query)
            supplier = Supplier(result[0],result[1],result[2],result[3],result[4])
            return supplier
        except mysql.connector.Error as error:
            return 'Excute thất bại !!!!'
    