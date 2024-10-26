-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3308
-- Generation Time: May 17, 2023 at 08:23 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `absen_karyawan`
--

-- --------------------------------------------------------

--
-- Table structure for table `absensi`
--

CREATE TABLE `absensi` (
  `id_absen` int(5) NOT NULL,
  `tanggal` date NOT NULL,
  `jam masuk` time NOT NULL,
  `jam pulang` time NOT NULL,
  `id_pegawai` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id_pegawai` int(5) NOT NULL,
  `username` varchar(12) NOT NULL,
  `password` varchar(16) NOT NULL,
  `nama` text NOT NULL,
  `jabatan` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `absensi`
--
ALTER TABLE `absensi`
  ADD PRIMARY KEY (`id_absen`),
  ADD KEY `fk_id_pegawai` (`id_pegawai`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id_pegawai`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `absensi`
--
ALTER TABLE `absensi`
  MODIFY `id_absen` int(5) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id_pegawai` int(5) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `absensi`
--
ALTER TABLE `absensi`
  ADD CONSTRAINT `fk_id_pegawai` FOREIGN KEY (`id_pegawai`) REFERENCES `user` (`id_pegawai`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
