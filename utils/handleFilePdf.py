from fpdf import FPDF
from DAO.medicineDAO import medicineDAO
from DAO.employeeDAO import employeeDAO
from DAO.supplierDAO import supplierDAO

class PDF(FPDF):
    def header(self):
        self.cell(0, 10, 'HÓA ĐƠN', border=False, align='C')
        self.ln(20)

    def contentOfPhieuNhap(self, pn, listCTPN):
        self.add_font('DejaVuSansCondensed', '', r"C:\fonts\DejaVuSansCondensed.ttf")
        self.set_font('DejaVuSansCondensed', size=10)

        nvDao = employeeDAO()
        nccDao = supplierDAO()
        nv = nvDao.getEmployeeById(pn.getMaNV())
        ncc = nccDao.getSupplierById(pn.getMaNCC())

        self.cell(80, 5, f'Hóa đơn #{pn.getMaPN()}')
        self.ln(7)
        self.cell(80, 5, f'Ngày tạo: {pn.getNgayTao()}')
        self.ln(7)
        self.cell(80, 5, f'Tên nhân viên: {nv.tennv}')
        self.ln(7)
        self.cell(80, 5, f'Tên nhà cung cấp: {ncc.getTenNCC()}')
        self.ln(15)
        line_height = self.font_size * 2.5
        col_width = self.epw/5
        header = ["Mã phiếu nhập", "Tên dược phẩm", "Số lượng", "Giá", "Thành tiền"]
        for i in header:
            self.multi_cell(col_width, line_height, i, border=1, ln=3, max_line_height=self.font_size)
        self.ln(line_height)
        dao = medicineDAO()
        for ctpn in listCTPN:
            medicine = dao.getMedicineById(ctpn.getMaDP())
            self.cell(col_width, line_height, str(ctpn.getMaPN()), border=1)
            self.cell(col_width, line_height, str(medicine.getTenDP()), border=1)
            self.cell(col_width, line_height, str(ctpn.getSoLuong()), border=1)
            self.cell(col_width, line_height, str(ctpn.getGia()), border=1)
            self.cell(col_width, line_height, str(ctpn.getThanhTien()), border=1)
            self.ln(line_height)

        self.cell(0, 10, f"Tổng tiền:         {pn.getTongTien()}",  align='R')

