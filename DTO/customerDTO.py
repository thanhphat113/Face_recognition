class customer:
    def __init__(self,makh,tenkh,gioitinh,sdt ,email):
        self.__makh=makh
        self.__tenkh=tenkh
        self.__gioitinh=gioitinh
        self.__email=email
        self.__sdt=sdt
    
    @property
    def makh(self):
        return self.__makh
    
    @makh.setter
    def makh(self,makh):
        self.__makh=makh
    
    @property
    def tenkh(self):
        return self.__tenkh
    
    @tenkh.setter
    def tenkh(self,tenkh):
        self.__tenkh=tenkh
    
    @property
    def gioitinh(self):
        return self.__gioitinh
    
    @gioitinh.setter
    def gioitinh(self, gioitinh):
        self.__gioitinh = gioitinh

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