import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DAO.employeeDAO import employeeDAO 
from DAO.supplierDAO import supplierDAO 
class PhieuNhap:
    def __init__(self, mapn, ngaytao, mancc,manv,tongtien):
        self.mapn = mapn
        self.manv = manv
        self.mancc = mancc
        self.ngaytao = ngaytao
        self.tongtien = tongtien
        self.ncc = None
        self.nhanvien = None

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
    
    def getNhanVien(self):
        empDAO = employeeDAO()
        self.nhanvien = empDAO.getEmployeeById(self.getMaNV())
        return self.nhanvien
    
    def getNCC(self):
        supDAO = supplierDAO()
        self.ncc = supDAO.getSupplierById(self.getMaNCC())
        return self.ncc

