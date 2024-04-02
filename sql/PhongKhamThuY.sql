-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: pkty
-- ------------------------------------------------------
-- Server version	8.0.33

create database PhongKhamThuY
use PhongKhamThuY

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `chitiet_hd`
--

DROP TABLE IF EXISTS `chitiet_hd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chitiet_hd` (
  `mahd` int DEFAULT NULL,
  `madv` int DEFAULT NULL,
  `soluong` int DEFAULT NULL,
  `gia` int DEFAULT NULL,
  KEY `fk_hoadon` (`mahd`),
  KEY `fk_hoadon_dichvu` (`madv`),
  CONSTRAINT `fk_hoadon` FOREIGN KEY (`mahd`) REFERENCES `hoadon` (`mahd`),
  CONSTRAINT `fk_hoadon_dichvu` FOREIGN KEY (`madv`) REFERENCES `dichvu` (`madv`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chitiet_hd`
--

LOCK TABLES `chitiet_hd` WRITE;
/*!40000 ALTER TABLE `chitiet_hd` DISABLE KEYS */;
/*!40000 ALTER TABLE `chitiet_hd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chitiet_pn`
--

DROP TABLE IF EXISTS `chitiet_pn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chitiet_pn` (
  `mapn` int DEFAULT NULL,
  `madp` int DEFAULT NULL,
  `soluong` int DEFAULT NULL,
  `tonggia` int DEFAULT NULL,
  KEY `fk_ncc_duocpham` (`madp`),
  KEY `fk_pn` (`mapn`),
  CONSTRAINT `fk_ncc_duocpham` FOREIGN KEY (`madp`) REFERENCES `duocpham` (`madp`),
  CONSTRAINT `fk_pn` FOREIGN KEY (`mapn`) REFERENCES `phieunhap` (`mapn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chitiet_pn`
--

LOCK TABLES `chitiet_pn` WRITE;
/*!40000 ALTER TABLE `chitiet_pn` DISABLE KEYS */;
/*!40000 ALTER TABLE `chitiet_pn` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dichvu`
--

DROP TABLE IF EXISTS `dichvu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dichvu` (
  `madv` int NOT NULL AUTO_INCREMENT,
  `tendv` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `giatien` int DEFAULT NULL,
  `maloaidv` int DEFAULT NULL,
  PRIMARY KEY (`madv`),
  KEY `loaidv_fk_idx` (`maloaidv`),
  CONSTRAINT `loaidv_fk` FOREIGN KEY (`maloaidv`) REFERENCES `loaidv` (`maloaidv`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dichvu`
--

LOCK TABLES `dichvu` WRITE;
/*!40000 ALTER TABLE `dichvu` DISABLE KEYS */;
/*!40000 ALTER TABLE `dichvu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dichvu_duocpham`
--

DROP TABLE IF EXISTS `dichvu_duocpham`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dichvu_duocpham` (
  `madv` int DEFAULT NULL,
  `madp` int DEFAULT NULL,
  KEY `fk_dichvu` (`madv`),
  KEY `fk_duocpham` (`madp`),
  CONSTRAINT `fk_dichvu` FOREIGN KEY (`madv`) REFERENCES `dichvu` (`madv`),
  CONSTRAINT `fk_duocpham` FOREIGN KEY (`madp`) REFERENCES `duocpham` (`madp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dichvu_duocpham`
--

LOCK TABLES `dichvu_duocpham` WRITE;
/*!40000 ALTER TABLE `dichvu_duocpham` DISABLE KEYS */;
/*!40000 ALTER TABLE `dichvu_duocpham` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `duocpham`
--

DROP TABLE IF EXISTS `duocpham`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `duocpham` (
  `madp` int NOT NULL AUTO_INCREMENT,
  `tendp` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `ngaysanxuat` date DEFAULT NULL,
  `ngayhethan` date DEFAULT NULL,
  `soluong` int DEFAULT NULL,
  `giathanh` int DEFAULT NULL,
  PRIMARY KEY (`madp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `duocpham`
--

LOCK TABLES `duocpham` WRITE;
/*!40000 ALTER TABLE `duocpham` DISABLE KEYS */;
/*!40000 ALTER TABLE `duocpham` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hoadon`
--

DROP TABLE IF EXISTS `hoadon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hoadon` (
  `mahd` int NOT NULL AUTO_INCREMENT,
  `ngaytao` date DEFAULT NULL,
  `tongtien` int DEFAULT NULL,
  `manv` int DEFAULT NULL,
  `makh` int DEFAULT NULL,
  PRIMARY KEY (`mahd`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hoadon`
--

LOCK TABLES `hoadon` WRITE;
/*!40000 ALTER TABLE `hoadon` DISABLE KEYS */;
/*!40000 ALTER TABLE `hoadon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `khachhang`
--

DROP TABLE IF EXISTS `khachhang`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `khachhang` (
  `makh` int NOT NULL AUTO_INCREMENT,
  `tenkh` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `gioitinh` tinyint(1) NOT NULL DEFAULT '0',
  `sdt` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`makh`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `khachhang`
--

LOCK TABLES `khachhang` WRITE;
/*!40000 ALTER TABLE `khachhang` DISABLE KEYS */;
/*!40000 ALTER TABLE `khachhang` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loaidv`
--

DROP TABLE IF EXISTS `loaidv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loaidv` (
  `maloaidv` int NOT NULL,
  `tenloai` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`maloaidv`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loaidv`
--

LOCK TABLES `loaidv` WRITE;
/*!40000 ALTER TABLE `loaidv` DISABLE KEYS */;
/*!40000 ALTER TABLE `loaidv` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loaitaikhoan`
--

DROP TABLE IF EXISTS `loaitaikhoan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loaitaikhoan` (
  `maloai` int NOT NULL AUTO_INCREMENT,
  `tenloai` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`maloai`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loaitaikhoan`
--

LOCK TABLES `loaitaikhoan` WRITE;
/*!40000 ALTER TABLE `loaitaikhoan` DISABLE KEYS */;
/*!40000 ALTER TABLE `loaitaikhoan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nhacungcap`
--

DROP TABLE IF EXISTS `nhacungcap`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nhacungcap` (
  `mancc` int NOT NULL AUTO_INCREMENT,
  `tenncc` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `diachi` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `sdt` varchar(11) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`mancc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nhacungcap`
--

LOCK TABLES `nhacungcap` WRITE;
/*!40000 ALTER TABLE `nhacungcap` DISABLE KEYS */;
/*!40000 ALTER TABLE `nhacungcap` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nhanvien`
--

DROP TABLE IF EXISTS `nhanvien`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nhanvien` (
  `manv` int NOT NULL AUTO_INCREMENT,
  `tennv` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `sdt` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `matk` int DEFAULT NULL,
  PRIMARY KEY (`manv`),
  KEY `FK_nhanvien_taikhoan` (`matk`),
  CONSTRAINT `FK_nhanvien_taikhoan` FOREIGN KEY (`matk`) REFERENCES `taikhoan` (`matk`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nhanvien`
--

LOCK TABLES `nhanvien` WRITE;
/*!40000 ALTER TABLE `nhanvien` DISABLE KEYS */;
/*!40000 ALTER TABLE `nhanvien` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phieunhap`
--

DROP TABLE IF EXISTS `phieunhap`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phieunhap` (
  `mapn` int NOT NULL AUTO_INCREMENT,
  `ngaytao` date DEFAULT NULL,
  `mancc` int DEFAULT NULL,
  `manv` int DEFAULT NULL,
  `tongtien` int DEFAULT NULL,
  PRIMARY KEY (`mapn`),
  KEY `fk_phieunhap_nhanvien` (`manv`),
  KEY `fk_phieunhap_ncc` (`mancc`),
  CONSTRAINT `fk_phieunhap_ncc` FOREIGN KEY (`mancc`) REFERENCES `nhacungcap` (`mancc`),
  CONSTRAINT `fk_phieunhap_nhanvien` FOREIGN KEY (`manv`) REFERENCES `nhanvien` (`manv`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phieunhap`
--

LOCK TABLES `phieunhap` WRITE;
/*!40000 ALTER TABLE `phieunhap` DISABLE KEYS */;
/*!40000 ALTER TABLE `phieunhap` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phongbenh`
--

DROP TABLE IF EXISTS `phongbenh`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phongbenh` (
  `mapb` int NOT NULL AUTO_INCREMENT,
  `tenpb` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `tinhtrang` tinyint(1) NOT NULL DEFAULT '1',
  `matn` int DEFAULT NULL,
  PRIMARY KEY (`mapb`),
  KEY `fk_phongbeng_thunuoi` (`matn`),
  CONSTRAINT `fk_phongbeng_thunuoi` FOREIGN KEY (`matn`) REFERENCES `thunuoi` (`matn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phongbenh`
--

LOCK TABLES `phongbenh` WRITE;
/*!40000 ALTER TABLE `phongbenh` DISABLE KEYS */;
/*!40000 ALTER TABLE `phongbenh` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `taikhoan`
--

DROP TABLE IF EXISTS `taikhoan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `taikhoan` (
  `matk` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `trangthai` tinyint(1) DEFAULT NULL,
  `maloai` int DEFAULT NULL,
  PRIMARY KEY (`matk`),
  KEY `fk_loaitaikhoan` (`maloai`),
  CONSTRAINT `fk_loaitaikhoan` FOREIGN KEY (`maloai`) REFERENCES `loaitaikhoan` (`maloai`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `taikhoan`
--

LOCK TABLES `taikhoan` WRITE;
/*!40000 ALTER TABLE `taikhoan` DISABLE KEYS */;
/*!40000 ALTER TABLE `taikhoan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `thunuoi`
--

DROP TABLE IF EXISTS `thunuoi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `thunuoi` (
  `matn` int NOT NULL AUTO_INCREMENT,
  `tentn` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `hinhanh` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `mau` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `cannang` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `loai` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `giong` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `gioitinh` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `makh` int DEFAULT NULL,
  PRIMARY KEY (`matn`),
  KEY `fk_thunuoi_khachhang` (`makh`),
  CONSTRAINT `fk_thunuoi_khachhang` FOREIGN KEY (`makh`) REFERENCES `khachhang` (`makh`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `thunuoi`
--

LOCK TABLES `thunuoi` WRITE;
/*!40000 ALTER TABLE `thunuoi` DISABLE KEYS */;
/*!40000 ALTER TABLE `thunuoi` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-27 17:23:56
