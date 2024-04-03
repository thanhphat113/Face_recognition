class loaitaikhoan:
    def __init__(self,maloai,tenloai):
        self.__maloai = maloai
        self.__tenloai = tenloai
        
    @property
    def maloai(self):
        return self.__maloai
    
    @maloai.setter
    def maloai(self,maloai):
        self.__maloai=maloai
    
    @property
    def tenloai(self):
        return self.__tenloai
    
    @tenloai.setter
    def tenloai(self,tenloai):
        self.__tenloai=tenloai