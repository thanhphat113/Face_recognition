from DAO.employeeDAO import employeeDAO 
from DAO.customerDAO import customerDAO 

class bill:
    max_mahd = 0
    def __init__(self, mahd : int, ngaytao : str, tongtien : int, manv : int, makh : int):
        self.__mahd = mahd
        self.__ngaytao = ngaytao
        self.__tongtien = tongtien
        self.__manv = manv
        self.__makh = makh
    
    def get_mahd(self):
        return self.__mahd
    
    def set_mahd(self, mahd):
        self.__mahd = mahd
    
    @classmethod
    def generate_mahd(cls):
        cls.max_mahd += 1
        return cls.max_mahd
    
    def get_ngaytao(self):
        return self.__ngaytao
    
    def set_ngaytao(self, ngaytao):
        self.__ngaytao = ngaytao
    
    def get_tongtien(self):
        return self.__tongtien
    
    def set_tongtien(self, tongtien):
        self.__tongtien = tongtien
    
    def get_manv(self):
        return self.__manv

    def get_makh(self):
        return self.__makh
    
    def getNhanVien(self):
        empDAO = employeeDAO()
        self.nhanvien = empDAO.getEmployeeById(self.get_manv())
        return self.nhanvien
    
    def getKH(self):
        cusDao = customerDAO()
        self.kh = cusDao.findByid(self.get_makh())
        return self.kh