-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 14, 2024 at 04:44 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5220411209`
--

-- --------------------------------------------------------

--
-- Table structure for table `kapalperang`
--

CREATE TABLE `kapalperang` (
  `id_kapal` int(6) NOT NULL,
  `Nama_Kapal` varchar(50) NOT NULL,
  `Asal_Negara` varchar(50) NOT NULL,
  `Tipe` enum('AircraftCarrier','BattleShip','Destroyer','Submarine') NOT NULL,
  `Class` varchar(50) NOT NULL,
  `Tahun_Ditugaskan` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `kapalperang`
--

INSERT INTO `kapalperang` (`id_kapal`, `Nama_Kapal`, `Asal_Negara`, `Tipe`, `Class`, `Tahun_Ditugaskan`) VALUES
(1, 'USS Yorktown', 'Amerika Serikat', 'AircraftCarrier', 'Yorktown', 1937),
(2, 'USS Saratoga', 'Amerika Serikat', 'AircraftCarrier', 'Lexington', 1927),
(6, 'USS Enterprise', 'Amerika Serikat', 'AircraftCarrier', 'Yorktown', 1938),
(7, 'IJN Akagi', 'Jepang', 'AircraftCarrier', '-', 1927),
(8, 'KMS Bismarck', 'Jerman', 'BattleShip', 'Bismarck', 1940),
(11, 'HMS Ark Royal', 'Inggris', 'AircraftCarrier', '-', 1938);

-- --------------------------------------------------------

--
-- Table structure for table `komandan`
--

CREATE TABLE `komandan` (
  `id_komandan` int(6) NOT NULL,
  `Nama_Komandan` varchar(50) NOT NULL,
  `Pangkat` enum('Commander','Captain','Admiral','Chief') NOT NULL,
  `id_kapal` int(6) NOT NULL,
  `Tahun_Dinas` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `komandan`
--

INSERT INTO `komandan` (`id_komandan`, `Nama_Komandan`, `Pangkat`, `id_kapal`, `Tahun_Dinas`) VALUES
(3, 'Elliott Buckmaster', 'Captain', 1, '1941-1942'),
(5, 'dasdsa', 'Commander', 7, '1941-1942'),
(7, 'George Dominic Murray', 'Captain', 6, '1941-1942'),
(8, 'DAS', 'Admiral', 1, '1941-1942'),
(10, 'Ernst Lindemann', 'Captain', 8, '1913-1941');

-- --------------------------------------------------------

--
-- Stand-in structure for view `komandandannamakapal`
-- (See below for the actual view)
--
CREATE TABLE `komandandannamakapal` (
`id_komandan` int(6)
,`Nama_Komandan` varchar(50)
,`Pangkat` enum('Commander','Captain','Admiral','Chief')
,`id_kapal` int(6)
,`Tahun_Dinas` varchar(50)
,`Nama_Kapal` varchar(50)
);

-- --------------------------------------------------------

--
-- Table structure for table `korbanjiwa`
--

CREATE TABLE `korbanjiwa` (
  `id_korbanjiwa` int(6) NOT NULL,
  `id_pertempuran` int(6) NOT NULL,
  `id_kapal` int(6) NOT NULL,
  `Tipe_Korban` enum('KorbanJiwa','KorbanHilang','KorbanLuka') NOT NULL,
  `JumlahKorban` int(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `pertempuran`
--

CREATE TABLE `pertempuran` (
  `id_pertempuran` int(6) NOT NULL,
  `Nama_Pertempuran` varchar(50) NOT NULL,
  `Tanggal_Pertempuran` varchar(50) NOT NULL,
  `Lokasi` varchar(50) NOT NULL,
  `Hasil_Pertempuran` varchar(50) NOT NULL,
  `id_kapal` int(6) NOT NULL,
  `id_komandan` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pertempuran`
--

INSERT INTO `pertempuran` (`id_pertempuran`, `Nama_Pertempuran`, `Tanggal_Pertempuran`, `Lokasi`, `Hasil_Pertempuran`, `id_kapal`, `id_komandan`) VALUES
(2, 'Battle of Leyte Gulf', '1941', 'Teluk Leyte', 'Kemenangan Sekutu', 8, 10),
(4, 'Battle of Midway', '1942-06-06', 'Midway Atoll', 'Kemenangan Sekutu', 6, 7),
(5, 'Battle of Santa Cruz', '1941', 'Santa Cruz', 'Kemenangan Sekutu', 6, 7),
(6, 'Battle of Guatemala', '1942', 'Guatemala', 'Kemenangan Sekutu', 2, 8),
(7, ' Battle of the Aleutian Islands', '1942', 'Kepulauan Aleutian', 'Kemenangan Sekutu', 6, 7);

-- --------------------------------------------------------

--
-- Structure for view `komandandannamakapal`
--
DROP TABLE IF EXISTS `komandandannamakapal`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `komandandannamakapal`  AS SELECT `komandan`.`id_komandan` AS `id_komandan`, `komandan`.`Nama_Komandan` AS `Nama_Komandan`, `komandan`.`Pangkat` AS `Pangkat`, `komandan`.`id_kapal` AS `id_kapal`, `komandan`.`Tahun_Dinas` AS `Tahun_Dinas`, `kapalperang`.`Nama_Kapal` AS `Nama_Kapal` FROM (`komandan` join `kapalperang` on(`komandan`.`id_kapal` = `kapalperang`.`id_kapal`)) ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `kapalperang`
--
ALTER TABLE `kapalperang`
  ADD PRIMARY KEY (`id_kapal`);

--
-- Indexes for table `komandan`
--
ALTER TABLE `komandan`
  ADD PRIMARY KEY (`id_komandan`),
  ADD KEY `id_kapal` (`id_kapal`);

--
-- Indexes for table `korbanjiwa`
--
ALTER TABLE `korbanjiwa`
  ADD PRIMARY KEY (`id_korbanjiwa`),
  ADD KEY `id_pertempuran` (`id_pertempuran`),
  ADD KEY `id_kapal` (`id_kapal`);

--
-- Indexes for table `pertempuran`
--
ALTER TABLE `pertempuran`
  ADD PRIMARY KEY (`id_pertempuran`),
  ADD KEY `id_kapal` (`id_kapal`),
  ADD KEY `id_komandan` (`id_komandan`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `kapalperang`
--
ALTER TABLE `kapalperang`
  MODIFY `id_kapal` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `komandan`
--
ALTER TABLE `komandan`
  MODIFY `id_komandan` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `korbanjiwa`
--
ALTER TABLE `korbanjiwa`
  MODIFY `id_korbanjiwa` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `pertempuran`
--
ALTER TABLE `pertempuran`
  MODIFY `id_pertempuran` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `komandan`
--
ALTER TABLE `komandan`
  ADD CONSTRAINT `komandan_ibfk_1` FOREIGN KEY (`id_kapal`) REFERENCES `kapalperang` (`id_kapal`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `korbanjiwa`
--
ALTER TABLE `korbanjiwa`
  ADD CONSTRAINT `korbanjiwa_ibfk_1` FOREIGN KEY (`id_kapal`) REFERENCES `kapalperang` (`id_kapal`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `korbanjiwa_ibfk_2` FOREIGN KEY (`id_pertempuran`) REFERENCES `pertempuran` (`id_pertempuran`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `pertempuran`
--
ALTER TABLE `pertempuran`
  ADD CONSTRAINT `pertempuran_ibfk_1` FOREIGN KEY (`id_kapal`) REFERENCES `kapalperang` (`id_kapal`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `pertempuran_ibfk_2` FOREIGN KEY (`id_komandan`) REFERENCES `komandan` (`id_komandan`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
