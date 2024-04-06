class bill:
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