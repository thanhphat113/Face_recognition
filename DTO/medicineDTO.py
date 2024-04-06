class Medicine:
    def __init__(self, madp, tendp, nsx, hsd, soluong, gia):
        self.madp = madp
        self.tendp = tendp
        self.nsx = nsx
        self.hsd = hsd
        self.soluong = soluong
        self.gia = gia

    def getMaDP(self):
        return self.madp
    
    def setMaDP(self, madp):
        self.madp = madp

    def getTenDP(self):
        return self.tendp
    
    def setTenDP(self, tendp):
        self.tendp = tendp

    def getNSX(self):
        return self.nsx
    
    def setNSX(self, nsx):
        self.nsx = nsx 

    def getHSD(self):
        return self.hsd
    
    def setHSD(self, hsd):
        self.hsd = hsd 

    def getSoLuong(self):
        return self.soluong
    
    def setSoLuong(self, soluong):
        self.soluong = soluong 

    def getGia(self):
        return self.gia
    
    def setGia(self, gia):
        self.gia = gia 


    