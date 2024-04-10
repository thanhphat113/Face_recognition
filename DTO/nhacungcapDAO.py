class nhacungcap:
    def __init__(self,mancc,tenncc,email,diachi,sdt):
        self.__mancc = mancc
        self.__tenncc = tenncc
        self.__email = email
        self.__diachi = diachi
        self.__sdt = sdt
        
    @property
    def mancc(self):
        return self.__mancc
    
    @mancc.setter
    def mancc(self,mancc):
        self.__mancc=mancc
    
    @property
    def tenncc(self):
        return self.__tenncc
    
    @tenncc.setter
    def manv(self,tenncc):
        self.__tenncc=tenncc
        
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def manv(self,email):
        self.__email=email
        
    @property
    def sdt(self):
        return self.__sdt
    
    @sdt.setter
    def sdt(self,sdt):
        self.__sdt=sdt
        
    @property
    def diachi(self):
        return self.__diachi
    
    @diachi.setter
    def diachi(self,diachi):
        self.__diachi=diachi 