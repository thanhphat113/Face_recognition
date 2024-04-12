class CTPN:
    def __init__(self, mactpn, mapn, madp, soluong, gia, thanhtien):
        self.mactpn = mactpn
        self.mapn = mapn
        self.madp = madp
        self.soluong = soluong
        self.gia = gia
        self.thanhtien = thanhtien

    def getMaCTPN(self):
        return self.mactpn
    
    def setMaCTPN(self, mactpn):
        self.mactpn = mactpn

    def getMaPN(self):
        return self.mapn
    
    def setMaPN(self, mapn):
        self.mapn = mapn
    
    def getMaDP(self):
        return self.madp
    
    def setMaDP(self, madp):
        self.madp = madp

    def getSoLuong(self):
        return self.soluong
    
    def setSoLuong(self, soluong):
        self.soluong = soluong 

    def getGia(self):
        return self.gia
    
    def setGia(self, gia):
        self.gia = gia 

    def getThanhTien(self):
        return self.thanhtien
    
    def setThanhTien(self, thanhtien):
        self.thanhtien = thanhtien 
