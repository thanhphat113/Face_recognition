-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: localhost
-- Thời gian đã tạo: Th4 03, 2024 lúc 09:14 AM
-- Phiên bản máy phục vụ: 10.4.28-MariaDB
-- Phiên bản PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `PhongKhamThuY`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `ChiTiet_HD`
--

CREATE TABLE `ChiTiet_HD` (
  `mahd` int(11) DEFAULT NULL,
  `madv` int(11) DEFAULT NULL,
  `soluong` int(11) DEFAULT NULL,
  `gia` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `ChiTiet_PN`
--

CREATE TABLE `ChiTiet_PN` (
  `mapn` int(11) DEFAULT NULL,
  `madp` int(11) DEFAULT NULL,
  `soluong` int(11) DEFAULT NULL,
  `tonggia` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `DichVu`
--

CREATE TABLE `DichVu` (
  `madv` int(11) NOT NULL,
  `tendv` varchar(255) DEFAULT NULL,
  `giatien` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `DichVu`
--

INSERT INTO `DichVu` (`madv`, `tendv`, `giatien`) VALUES
(1, 'Khám bệnh', 200000),
(2, 'Chữa bệnh', 500000),
(3, 'Tiêm phòng', 150000),
(4, 'Phẫu thuật', 1000000),
(5, 'Chẩn đoán hình ảnh', 300000),
(6, 'Xét nghiệm máu', 250000),
(7, 'Vệ sinh răng', 80000),
(8, 'Tư vấn dinh dưỡng', 120000),
(9, 'Massage', 180000),
(10, 'Chăm sóc da', 160000);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `DichVu_DuocPham`
--

CREATE TABLE `DichVu_DuocPham` (
  `madv` int(11) DEFAULT NULL,
  `madp` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `DichVu_DuocPham`
--

INSERT INTO `DichVu_DuocPham` (`madv`, `madp`) VALUES
(3, 1),
(3, 2);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `DuocPham`
--

CREATE TABLE `DuocPham` (
  `madp` int(11) NOT NULL,
  `tendp` varchar(255) DEFAULT NULL,
  `ngaysanxuat` date DEFAULT NULL,
  `ngayhethan` date DEFAULT NULL,
  `soluong` int(11) DEFAULT NULL,
  `giathanh` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `DuocPham`
--

INSERT INTO `DuocPham` (`madp`, `tendp`, `ngaysanxuat`, `ngayhethan`, `soluong`, `giathanh`) VALUES
(1, 'Thuốc A', '2023-01-01', '2024-01-01', 100, 50000),
(2, 'Thuốc B', '2022-05-10', '2023-05-10', 50, 75000),
(3, 'Thuốc C', '2023-03-15', '2024-03-15', 80, 60000),
(4, 'Thuốc D', '2023-02-20', '2024-02-20', 120, 45000),
(5, 'Thuốc E', '2022-11-11', '2023-11-11', 70, 70000),
(6, 'Thuốc F', '2022-09-05', '2023-09-05', 90, 55000),
(7, 'Thuốc G', '2023-07-20', '2024-07-20', 110, 65000),
(8, 'Thuốc H', '2023-04-25', '2024-04-25', 60, 80000),
(9, 'Thuốc I', '2022-12-12', '2023-12-12', 85, 70000),
(10, 'Thuốc K', '2023-10-30', '2024-10-30', 95, 60000);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `HoaDon`
--

CREATE TABLE `HoaDon` (
  `mahd` int(11) NOT NULL,
  `ngaytao` date DEFAULT NULL,
  `tongtien` int(11) DEFAULT NULL,
  `manv` int(11) DEFAULT NULL,
  `makh` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `KhachHang`
--

CREATE TABLE `KhachHang` (
  `makh` int(11) NOT NULL,
  `tenkh` varchar(255) DEFAULT NULL,
  `gioitinh` tinyint(1) NOT NULL DEFAULT 0,
  `sdt` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `KhachHang`
--

INSERT INTO `KhachHang` (`makh`, `tenkh`, `gioitinh`, `sdt`, `email`) VALUES
(1, 'Nguyễn Văn A', 1, '0987654321', 'nguyenvana@example.com'),
(2, 'Trần Thị B', 0, '0901234567', 'tranthib@example.com'),
(3, 'Lê Văn C', 1, '0912345678', 'levanc@example.com'),
(4, 'Phạm Thị D', 0, '0923456789', 'phamthid@example.com'),
(5, 'Hoàng Văn E', 1, '0934567890', 'hoangvane@example.com'),
(6, 'Mai Thị F', 0, '0945678901', 'maithif@example.com'),
(7, 'Vũ Văn G', 1, '0956789012', 'vuvang@example.com'),
(8, 'Lương Thị H', 0, '0967890123', 'luongthih@example.com'),
(9, 'Đặng Văn I', 1, '0978901234', 'dangvani@example.com'),
(10, 'Lê Thị K', 0, '0989012345', 'lethik@example.com');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `LoaiTaiKhoan`
--

CREATE TABLE `LoaiTaiKhoan` (
  `maloai` int(11) NOT NULL,
  `tenloai` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `LoaiTaiKhoan`
--

INSERT INTO `LoaiTaiKhoan` (`maloai`, `tenloai`) VALUES
(1, 'admin'),
(2, 'Nhân viên');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `NhaCungCap`
--

CREATE TABLE `NhaCungCap` (
  `mancc` int(11) NOT NULL,
  `tenncc` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `diachi` varchar(255) DEFAULT NULL,
  `sdt` varchar(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `NhaCungCap`
--

INSERT INTO `NhaCungCap` (`mancc`, `tenncc`, `email`, `diachi`, `sdt`) VALUES
(1, 'Nhà cung cấp A', 'nhacungcapA@example.com', 'Địa chỉ A', '0123456789'),
(2, 'Nhà cung cấp B', 'nhacungcapB@example.com', 'Địa chỉ B', '0987654321'),
(3, 'Nhà cung cấp C', 'nhacungcapC@example.com', 'Địa chỉ C', '0123987654'),
(4, 'Nhà cung cấp D', 'nhacungcapD@example.com', 'Địa chỉ D', '0987123456'),
(5, 'Nhà cung cấp E', 'nhacungcapE@example.com', 'Địa chỉ E', '0123456789'),
(6, 'Nhà cung cấp F', 'nhacungcapF@example.com', 'Địa chỉ F', '0987654321'),
(7, 'Nhà cung cấp G', 'nhacungcapG@example.com', 'Địa chỉ G', '0123987654'),
(8, 'Nhà cung cấp H', 'nhacungcapH@example.com', 'Địa chỉ H', '0987123456'),
(9, 'Nhà cung cấp I', 'nhacungcapI@example.com', 'Địa chỉ I', '0123456789'),
(10, 'Nhà cung cấp J', 'nhacungcapJ@example.com', 'Địa chỉ J', '0987654321');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `NhanVien`
--

CREATE TABLE `NhanVien` (
  `manv` int(11) NOT NULL,
  `tennv` varchar(255) DEFAULT NULL,
  `sdt` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `matk` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `NhanVien`
--

INSERT INTO `NhanVien` (`manv`, `tennv`, `sdt`, `email`, `matk`) VALUES
(1, 'Thanh phát', '089842525', 'thanhphat9523@gmail.com', 1),
(2, 'Nguyễn Văn X', '0987654321', 'nguyenvanx@example.com', 1),
(3, 'Trần Thị Y', '0901234567', 'tranthiy@example.com', 1),
(4, 'Lê Văn Z', '0912345678', 'levanz@example.com', 1),
(5, 'Phạm Thị T', '0923456789', 'phamthit@example.com', 1),
(6, 'Hoàng Văn S', '0934567890', 'hoangvans@example.com', 1),
(7, 'Mai Thị R', '0945678901', 'maithir@example.com', 1),
(8, 'Vũ Văn Q', '0956789012', 'vuvanq@example.com', 1),
(9, 'Lương Thị P', '0967890123', 'luongthip@example.com', 1),
(10, 'Đặng Văn O', '0978901234', 'dangvano@example.com', 1),
(11, 'Lê Thị N', '0989012345', 'lethin@example.com', 1);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `PhieuNhap`
--

CREATE TABLE `PhieuNhap` (
  `mapn` int(11) NOT NULL,
  `ngaytao` date DEFAULT NULL,
  `mancc` int(11) DEFAULT NULL,
  `manv` int(11) DEFAULT NULL,
  `tongtien` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `PhongBenh`
--

CREATE TABLE `PhongBenh` (
  `mapb` int(11) NOT NULL,
  `tenpb` varchar(255) DEFAULT NULL,
  `tinhtrang` tinyint(1) NOT NULL DEFAULT 1,
  `matn` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `PhongBenh`
--

INSERT INTO `PhongBenh` (`mapb`, `tenpb`, `tinhtrang`, `matn`) VALUES
(1, 'Phòng A', 1, NULL),
(2, 'Phòng B', 0, 2),
(3, 'Phòng C', 0, 3),
(4, 'Phòng D', 0, 4),
(5, 'Phòng E', 1, NULL),
(6, 'Phòng F', 1, 6),
(7, 'Phòng G', 0, 7),
(8, 'Phòng H', 0, 8),
(9, 'Phòng I', 1, NULL),
(10, 'Phòng J', 1, NULL);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `TaiKhoan`
--

CREATE TABLE `TaiKhoan` (
  `matk` int(11) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `trangthai` tinyint(1) DEFAULT NULL,
  `maloai` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `TaiKhoan`
--

INSERT INTO `TaiKhoan` (`matk`, `username`, `password`, `trangthai`, `maloai`) VALUES
(1, 'thanhphat', '123', 1, 1),
(2, 'nguyenvanx', 'password1', 1, 2),
(3, 'tranthiy', 'password2', 1, 2),
(4, 'levanz', 'password3', 1, 2),
(5, 'phamthit', 'password4', 1, 2),
(6, 'hoangvans', 'password5', 1, 2),
(7, 'maithir', 'password6', 1, 2),
(8, 'vuvanq', 'password7', 1, 2),
(9, 'luongthip', 'password8', 1, 2),
(10, 'dangvano', 'password9', 1, 2),
(11, 'lethin', 'password10', 1, 2),
(12, 'admin', 'admin', 1, 1);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `ThuNuoi`
--

CREATE TABLE `ThuNuoi` (
  `matn` int(11) NOT NULL,
  `tentn` varchar(255) DEFAULT NULL,
  `mau` varchar(255) DEFAULT NULL,
  `cannang` varchar(255) DEFAULT NULL,
  `makh` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `ThuNuoi`
--

INSERT INTO `ThuNuoi` (`matn`, `tentn`, `mau`, `cannang`, `makh`) VALUES
(1, 'Mèo Kitty', 'Trắng', '5 kg', 1),
(2, 'Chó La La', 'Nâu', '10 kg', 2),
(3, 'Chim Cút', 'Đen', '0.5 kg', 3),
(4, 'Hà Cảo', 'Vàng', '0.3 kg', 4),
(5, 'Rùa Rồng', 'Xanh', '3 kg', 5),
(6, 'Chim Cánh Cụt', 'Hồng', '2 kg', 6),
(7, 'Hươu Cao Cổ', 'Nâu', '100 kg', 7),
(8, 'Khỉ Đuôi Dài', 'Nâu', '15 kg', 8),
(9, 'Gấu Trúc', 'Trắng đen', '80 kg', 9),
(10, 'Sư Tử', 'Vàng', '150 kg', 10);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `ChiTiet_HD`
--
ALTER TABLE `ChiTiet_HD`
  ADD KEY `fk_hoadon` (`mahd`),
  ADD KEY `fk_hoadon_dichvu` (`madv`);

--
-- Chỉ mục cho bảng `ChiTiet_PN`
--
ALTER TABLE `ChiTiet_PN`
  ADD KEY `fk_ncc_duocpham` (`madp`),
  ADD KEY `fk_pn` (`mapn`);

--
-- Chỉ mục cho bảng `DichVu`
--
ALTER TABLE `DichVu`
  ADD PRIMARY KEY (`madv`);

--
-- Chỉ mục cho bảng `DichVu_DuocPham`
--
ALTER TABLE `DichVu_DuocPham`
  ADD KEY `fk_dichvu` (`madv`),
  ADD KEY `fk_duocpham` (`madp`);

--
-- Chỉ mục cho bảng `DuocPham`
--
ALTER TABLE `DuocPham`
  ADD PRIMARY KEY (`madp`);

--
-- Chỉ mục cho bảng `HoaDon`
--
ALTER TABLE `HoaDon`
  ADD PRIMARY KEY (`mahd`);

--
-- Chỉ mục cho bảng `KhachHang`
--
ALTER TABLE `KhachHang`
  ADD PRIMARY KEY (`makh`);

--
-- Chỉ mục cho bảng `LoaiTaiKhoan`
--
ALTER TABLE `LoaiTaiKhoan`
  ADD PRIMARY KEY (`maloai`);

--
-- Chỉ mục cho bảng `NhaCungCap`
--
ALTER TABLE `NhaCungCap`
  ADD PRIMARY KEY (`mancc`);

--
-- Chỉ mục cho bảng `NhanVien`
--
ALTER TABLE `NhanVien`
  ADD PRIMARY KEY (`manv`),
  ADD KEY `FK_nhanvien_taikhoan` (`matk`);

--
-- Chỉ mục cho bảng `PhieuNhap`
--
ALTER TABLE `PhieuNhap`
  ADD PRIMARY KEY (`mapn`),
  ADD KEY `fk_phieunhap_nhanvien` (`manv`),
  ADD KEY `fk_phieunhap_ncc` (`mancc`);

--
-- Chỉ mục cho bảng `PhongBenh`
--
ALTER TABLE `PhongBenh`
  ADD PRIMARY KEY (`mapb`),
  ADD KEY `fk_phongbeng_thunuoi` (`matn`);

--
-- Chỉ mục cho bảng `TaiKhoan`
--
ALTER TABLE `TaiKhoan`
  ADD PRIMARY KEY (`matk`),
  ADD KEY `fk_loaitaikhoan` (`maloai`);

--
-- Chỉ mục cho bảng `ThuNuoi`
--
ALTER TABLE `ThuNuoi`
  ADD PRIMARY KEY (`matn`),
  ADD KEY `fk_thunuoi_khachhang` (`makh`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `DichVu`
--
ALTER TABLE `DichVu`
  MODIFY `madv` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT cho bảng `DuocPham`
--
ALTER TABLE `DuocPham`
  MODIFY `madp` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT cho bảng `HoaDon`
--
ALTER TABLE `HoaDon`
  MODIFY `mahd` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `KhachHang`
--
ALTER TABLE `KhachHang`
  MODIFY `makh` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT cho bảng `LoaiTaiKhoan`
--
ALTER TABLE `LoaiTaiKhoan`
  MODIFY `maloai` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT cho bảng `NhaCungCap`
--
ALTER TABLE `NhaCungCap`
  MODIFY `mancc` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT cho bảng `NhanVien`
--
ALTER TABLE `NhanVien`
  MODIFY `manv` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT cho bảng `PhieuNhap`
--
ALTER TABLE `PhieuNhap`
  MODIFY `mapn` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `PhongBenh`
--
ALTER TABLE `PhongBenh`
  MODIFY `mapb` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT cho bảng `TaiKhoan`
--
ALTER TABLE `TaiKhoan`
  MODIFY `matk` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT cho bảng `ThuNuoi`
--
ALTER TABLE `ThuNuoi`
  MODIFY `matn` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `ChiTiet_HD`
--
ALTER TABLE `ChiTiet_HD`
  ADD CONSTRAINT `fk_hoadon` FOREIGN KEY (`mahd`) REFERENCES `HoaDon` (`mahd`),
  ADD CONSTRAINT `fk_hoadon_dichvu` FOREIGN KEY (`madv`) REFERENCES `DichVu` (`madv`);

--
-- Các ràng buộc cho bảng `ChiTiet_PN`
--
ALTER TABLE `ChiTiet_PN`
  ADD CONSTRAINT `fk_ncc_duocpham` FOREIGN KEY (`madp`) REFERENCES `DuocPham` (`madp`),
  ADD CONSTRAINT `fk_pn` FOREIGN KEY (`mapn`) REFERENCES `PhieuNhap` (`mapn`);

--
-- Các ràng buộc cho bảng `DichVu_DuocPham`
--
ALTER TABLE `DichVu_DuocPham`
  ADD CONSTRAINT `fk_dichvu` FOREIGN KEY (`madv`) REFERENCES `DichVu` (`madv`),
  ADD CONSTRAINT `fk_duocpham` FOREIGN KEY (`madp`) REFERENCES `DuocPham` (`madp`);

--
-- Các ràng buộc cho bảng `NhanVien`
--
ALTER TABLE `NhanVien`
  ADD CONSTRAINT `FK_nhanvien_taikhoan` FOREIGN KEY (`matk`) REFERENCES `TaiKhoan` (`matk`);

--
-- Các ràng buộc cho bảng `PhieuNhap`
--
ALTER TABLE `PhieuNhap`
  ADD CONSTRAINT `fk_phieunhap_ncc` FOREIGN KEY (`mancc`) REFERENCES `NhaCungCap` (`mancc`),
  ADD CONSTRAINT `fk_phieunhap_nhanvien` FOREIGN KEY (`manv`) REFERENCES `NhanVien` (`manv`);

--
-- Các ràng buộc cho bảng `PhongBenh`
--
ALTER TABLE `PhongBenh`
  ADD CONSTRAINT `fk_phongbeng_thunuoi` FOREIGN KEY (`matn`) REFERENCES `ThuNuoi` (`matn`);

--
-- Các ràng buộc cho bảng `TaiKhoan`
--
ALTER TABLE `TaiKhoan`
  ADD CONSTRAINT `fk_loaitaikhoan` FOREIGN KEY (`maloai`) REFERENCES `LoaiTaiKhoan` (`maloai`);

--
-- Các ràng buộc cho bảng `ThuNuoi`
--
ALTER TABLE `ThuNuoi`
  ADD CONSTRAINT `fk_thunuoi_khachhang` FOREIGN KEY (`makh`) REFERENCES `KhachHang` (`makh`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
