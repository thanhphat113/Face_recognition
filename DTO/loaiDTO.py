class loai:
    def __init__(self, maloai, tenloai):
        self.__maLoai = maloai
        self.__tenLoai = tenloai
        
    @property
    def maLoai(self):
        return self.__maLoai
    
    @maLoai.setter
    def maLoai(self,maloai):
        self.__maLoai=maloai
    
    @property
    def tenLoai(self):
        return self.__tenLoai
    
    @tenLoai.setter
    def tenLoai(self,tenLoai):
        self.__tenLoai=tenLoai