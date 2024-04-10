class employee:
    def __init__(self,manv,tennv,sdt ,email,matk):
        self.__manv=manv
        self.__tennv=tennv
        self.__email=email
        self.__sdt=sdt
        self.__matk=matk
    
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
        
    @property
    def matk(self):
        return self.__matk
    
    @matk.setter
    def matk(self,matk):
        self.__matk=matk
        