class taikhoan:
    max_matk = 0

    def __init__(self, matk : int, username : str, password : str, trangthai : int, maloai : int):
        self.__matk = matk
        self.__username = username
        self.__password = password
        self.__trangthai = trangthai
        self.__maloai = maloai
        
    @property
    def matk(self):
        return self.__matk
    
    @matk.setter
    def matk(self,matk):
        self.__matk=matk
        
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self,username):
        self.__username=username
        
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self,password):
        self.__password=password
        
    @property
    def trangthai(self):
        return self.__trangthai
    
    @trangthai.setter
    def trangthai(self,trangthai):
        self.__trangthai=trangthai
        
    @property
    def maloai(self):
        return self.__maloai
    
    @maloai.setter
    def maloai(self,maloai):
        self.__maloai=maloai

    @classmethod
    def generate_manv(cls):
        cls.max_matk += 1
        return cls.max_matk