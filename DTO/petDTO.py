import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DAO.customerDAO import customerDAO
class pet:
    def __init__(self, matn : int, tentn : str, maulong : str, cannang : str, makh : int):
        self.__matn = matn
        self.__tentn = tentn
        self.__maulong = maulong
        self.__cannang = cannang
        self.__makh = makh
        self.__khachhang = None

    
    def get_matn(self):
        return self.__matn
    
    def set_matn(self, matn):
        self.__matn=matn
    
    def get_tentn(self):
        return self.__tentn
    
    def set_tentn(self, tentn):
        self.__tentn = tentn

    def get_maulong(self):
        return self.__maulong
    
    def set_maulong(self, maulong):
        self.__maulong = maulong
    
    def get_cannang(self):
        return self.__cannang
    
    def set_cannang(self, cannang):
        self.__cannang = cannang
    
    def get_makh(self):
        return self.__makh
    
    def set_makh(self,makh):
        self.__makh=makh
        
    def get_khachhang(self):
        cus = customerDAO()
        self.__khachhang = cus.findByid(self.get_makh())
        return self.__khachhang
    