import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DAO.petDAO import petDAO

class phongbenh:
    def __init__(self,mapb,tenpb,tinhtrang,matn):
        self.__mapb = mapb
        self.__tenpb = tenpb
        self.__tinhtrang = tinhtrang
        self.__matn = matn
        self.__thunuoi = None
    
    @property
    def mapb(self):
        return self.__mapb
    
    @mapb.setter
    def mapb(self,mapb):
        self.__mapb=mapb
        
    @property
    def tenpb(self):
        return self.__tenpb
    
    @tenpb.setter
    def tenpb(self,tenpb):
        self.__tenpb=tenpb
    
    @property
    def tinhtrang(self):
        if self.__tinhtrang == 0: return "<Đang sử dụng>"
        return "<Còn trống>"
    
    @tinhtrang.setter
    def tinhtrang(self,tinhtrang):
        self.__tinhtrang=tinhtrang
        
    @property
    def matn(self):
        return self.__matn
    
    @matn.setter
    def matn(self,matn):
        self.__matn=matn
    
    @property
    def thunuoi(self):
        pet = petDAO()
        self.__thunuoi = pet.findById(self.__matn)
        return self.__thunuoi
    
    @thunuoi.setter
    def thunuoi(self,thunuoi):
        self.__thunuoi=thunuoi
        
if __name__ == "__main__":
    pb = phongbenh(1,'aaa',0,1)
    print(pb.thunuoi.get_tentn())
    
        