class Supplier:
    def __init__(self, mancc, tenncc, email, diachi, sdt):
        self.mancc = mancc
        self.tenncc = tenncc
        self.email = email
        self.diachi = diachi
        self.sdt = sdt

    def getMaNCC(self):
        return self.mancc
    
    def setMaNCC(self, mancc):
        self.mancc = mancc
    
    def getTenNCC(self):
        return self.tenncc
    
    def setTenNCC(self, tenncc):
        self.tenncc = tenncc

    def getEmail(self):
        return self.email
    
    def setEmail(self, email):
        self.email = email

    def getDiaChi(self):
        return self.diachi
    
    def setDiaChi(self, diachi):
        self.diachi = diachi

    def getSdt(self):
        return self.sdt
    
    def setSdt(self, sdt):
        self.sdt = sdt
