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
    