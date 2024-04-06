class PhieuNhap:
    def __init__(self, mapn, manv, mancc, ngaytao, tongtien):
        self.mapn = mapn
        self.manv = manv
        self.mancc = mancc
        self.ngaytao = ngaytao
        self.tongtien = tongtien

    def getMaPN(self):
        return self.mapn
    
    def setMaPN(self, mapn):
        self.mapn = mapn
    
    def getMaNV(self):
        return self.manv
    
    def setMaNV(self, manv):
        self.manv = manv

    def getMaNCC(self):
        return self.mancc
    
    def setMaNCC(self, mancc):
        self.mancc = mancc

    def getNgayTao(self):
        return self.ngaytao
    
    def setNgayTao(self, ngaytao):
        self.ngaytao = ngaytao

    def getTongTien(self):
        return self.tongtien
    
    def setTongTien(self, tongtien):
        self.tongtien = tongtien
