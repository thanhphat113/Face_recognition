class employee:
    def __init__(self,manv,tennv,email,sdt):
        self.manv=manv
        self.tennv=tennv
        self.email=email
        self.sdt=sdt
    
    def getmanv(self):
        return self.manv
    
    def setManv(self,manv):
        self.manv=manv
        
    def getTennv(self):
        return self.tennv
    
    def setTennv(self,tennv):
        self.tennv=tennv
        
    def getEmail(self):
        return self.email
    
    def setEmail(self,email):
        self.email=email
        
    def getSdt(self):
        return self.sdt
    
    def setSdt(self,sdt):
        self.sdt=sdt