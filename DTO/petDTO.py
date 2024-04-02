from DTO.customerDTO import customer

class pet:
    
    def __init__(self, matn : str, tentn : str, maulong : str, cannang : int, loai : str, giong : str, gioitinh : str, kh : str, hinhanh : str):
        self.__matn = matn
        self.__tentn = tentn
        self.__maulong = maulong
        self.__cannang = cannang
        self.__loai = loai
        self.__giong = giong
        self.__gioitinh = gioitinh
        self.__kh = kh
        self.__hinhanh = hinhanh
    
    def get_matn(self):
        return self.__matn

    
    def get_tentn(self):
        return self.__tentn
    
    def set_tentn(self, tentn):
        self.__tentn = tentn
    #--------------------------------------------------------
    def get_maulong(self):
        return self.__maulong
    
    def set_maulong(self, maulong):
        self.__maulong = maulong
    
    def get_cannang(self):
        return self.__cannang
    
    def set_cannang(self, cannang):
        self.__cannang = cannang
    

    def get_loai(self):
        return self.__loai
    
    def set_loai(self, loai):
        self.__loai = loai
    
    
    def get_giong(self):
        return self.__giong
    
    def set_giong(self, giong):
        self.__giong = giong
    
    def get_gioitinh(self):
        return self.__gioitinh
    
    def set_gioitinh(self, gioitinh):
        self.__gioitinh = gioitinh
    
    def get_kh(self):
        return self.__kh
    

    def get_hinhanh(self):
        return self.__hinhanh
    
    def set_hinhanh(self, hinhanh):
        self.__hinhanh = hinhanh
    
    