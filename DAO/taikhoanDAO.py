import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import DAO.database as db
from DTO.taikhoanDTO import taikhoan



class taikhoanDAO:
    def __init__(self):
        self.conn = db.connect_to_database()
        
    def checkPassword(self,username,password):
        try:
            self.conn.connect()
            query = f"Select * from TaiKhoan where username = '{username}' and password = '{password}'"
            result = db.execute_fetch_all(self.conn,query)
            if not result:
                return None
            for tk in result:
                account = taikhoan(tk[0],tk[1],tk[2],tk[3],tk[4])
            return account.maloai
        except mysql.connector.Error as error:
            return error
        finally:
            self.conn.close()
        
            
if __name__ == "__main__":
    example = 'admin'
    passw = 'admin'
    tkDAO = taikhoanDAO()
    aa = tkDAO.checkPassword(example,passw)
    print(aa)
    
        
    