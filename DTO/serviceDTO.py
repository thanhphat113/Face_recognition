class Service:
    def __init__(self, madv, ten, gia):
        self.madv = madv
        self.ten = ten
        self.gia = gia

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
