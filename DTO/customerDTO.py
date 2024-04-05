class customer:
    def __init__(self, makh : int, tenkh : str, gioitinh : int, sdt : str, email : str):
        self.__makh = makh
        self.__tenkh = tenkh
        self.__loaigt = gioitinh
        self.__email = email
        self.__sdt = sdt
    
    
    def get_loaigt(self):
        return self.__loaigt
    
    def set_loaigt(self, loaigt):
        self.__loaigt = loaigt
    
    def get_makh(self):
        return self.__makh
    
    def set_makh(self, makh):
        self.__makh = makh
    
    def get_tenkh(self):
        return self.__tenkh
    
    def set_tenkh(self, tenkh):
        self.__tenkh = tenkh
    
    def get_gioitinh(self):
        if self.__loaigt == 0: return "Nữ"
        return "Nam"
    

    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email
    
    def get_sdt(self):
        return self.__sdt
    
    def set_sdt(self, sdt):
        self.__sdt = sdt