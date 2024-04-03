class Service:
    def __init__(self, madv, ten, gia, maloaidv):
        self.madv = madv
        self.ten = ten
        self.gia = gia
        self.maloaidv = maloaidv

    def getMaDV(self):
        return self.madv
    
    def setMaDV(self, madv):
        self.madv = madv
    
    def getTen(self):
        return self.ten
    
    def setTen(self, ten):
        self.ten = ten

    def getGia(self):
        return self.gia
    
    def setGia(self, gia):
        self.gia = gia
    
    def getMaLoaiDV(self):
        return self.maloaidv
    
    def setMaLoaiDV(self, maloaidv):
        self.maloaidv = maloaidv