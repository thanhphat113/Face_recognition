import itertools

class ServiceCategory():
    def __init__(self, maloaidv, tenloai):
        self.maloaidv = maloaidv
        self.tenloai = tenloai

    def getMaLoaiDV(self):
        return self.maloaidv
    
    def setMaLoaiDV(self, maloaidv):
        self.maloaidv = maloaidv
    
    def getTenLoai(self):
        return self.tenloai
    
    def setTenLoai(self, tenloai):
        self.tenloai = tenloai