class pet:
    def __init__(self, matn : int, tentn : str, maulong : str, cannang : str, loai : str, giong : str, gioitinh : str, kh : int):
        self.__matn = matn
        self.__tentn = tentn
        self.__maulong = maulong
        self.__cannang = cannang
        self.__loai = loai
        self.__giong = giong
        self.__gioitinh = gioitinh
        self.__kh = kh
    
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
    
    
    