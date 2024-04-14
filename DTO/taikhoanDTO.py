import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DAO.employeeDAO import employeeDAO
from DAO.loaitaikhoanDAO import loaitaikhoanDAO

class taikhoan:
    def __init__(self, matk : int, username : str, password : str, trangthai : int, maloai : int,manv:int):
        self.__matk = matk
        self.__username = username
        self.__password = password
        self.__trangthai = trangthai
        self.__maloai = maloai
        self.__manv = manv
        self.__nhanvien = None
        self.__loai = None
        
    @property
    def matk(self):
        return self.__matk
    
    @matk.setter
    def matk(self,matk):
        self.__matk=matk
        
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self,username):
        self.__username=username
        
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self,password):
        self.__password=password
        
    @property
    def trangthai(self):
        return self.__trangthai
    
    @trangthai.setter
    def trangthai(self,trangthai):
        self.__trangthai=trangthai
        
    @property
    def maloai(self):
        return self.__maloai
    
    @maloai.setter
    def maloai(self,maloai):
        self.__maloai=maloai
        
    @property
    def manv(self):
        return self.__manv
    
    @manv.setter
    def manv(self,manv):
        self.__manv=manv

    @property
    def nhanvien(self):
        empDAO = employeeDAO()
        self.__nhanvien = empDAO.getEmployeeById(self.manv)
        return self.__nhanvien
    
    @property
    def loai(self):
        ltkDAO = loaitaikhoanDAO()
        self.__loai = ltkDAO.findById(self.maloai)
        return self.__loai