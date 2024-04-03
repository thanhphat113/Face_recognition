class employee:
    max_manv = 0
    def __init__(self,manv,tennv,sdt ,email):
        self.__manv=manv
        self.__tennv=tennv
        self.__email=email
        self.__sdt=sdt
    
    @property
    def manv(self):
        return self.__manv
    
    @manv.setter
    def manv(self,manv):
        self.__manv=manv
    
    @property
    def tennv(self):
        return self.__tennv
    
    @tennv.setter
    def tennv(self,tennv):
        self.__tennv=tennv
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,email):
        self.__email=email
    
    @property
    def sdt(self):
        return self.__sdt
    
    @sdt.setter
    def sdt(self,sdt):
        self.__sdt=sdt
        
    @classmethod
    def generate_manv(cls):
        # Tăng giá trị của max_manv lên 1 và trả về giá trị mới
        cls.max_manv += 1
        return cls.max_manv