-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 28, 2023 at 12:05 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `h20webmonitor`
--

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `rid` int(11) NOT NULL,
  `farmername` varchar(50) NOT NULL,
  `adharnumber` varchar(20) NOT NULL,
  `age` int(100) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `phonenumber` varchar(12) NOT NULL,
  `address` varchar(50) NOT NULL,
  `farming` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Triggers `register`
--
DELIMITER $$
CREATE TRIGGER `deletion` BEFORE DELETE ON `register` FOR EACH ROW INSERT INTO trig VALUES(null,OLD.rid,'FARMER DELETED',NOW())
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `insertion` AFTER INSERT ON `register` FOR EACH ROW INSERT INTO trig VALUES(null,NEW.rid,'Farmer Inserted',NOW())
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `updation` AFTER UPDATE ON `register` FOR EACH ROW INSERT INTO trig VALUES(null,NEW.rid,'FARMER UPDATED',NOW())
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `report`
--

CREATE TABLE `report` (
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `pid` int(11) NOT NULL,
  `productname` varchar(100) NOT NULL,
  `productdesc` text NOT NULL,
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `report`
--

INSERT INTO `report` (`username`, `email`, `pid`, `productname`, `productdesc`, `price`) VALUES
('h2owebmonitor', 'h2oweb001@gmail.com', 1, 'REMOTE SENSING', 'Facing an issue in or Think its inappropriate.\r\nPlease do reach us out.', 0),
('h2owebmonitor', 'h2oweb001@gmail.com', 2, 'ML Forecasting', 'Facing an issue in or Think its inappropriate.\r\nPlease do reach us out. ', 0),
('h2owebmonitor', 'h2oweb001@gmail.com', 3, 'Image Processing', 'Facing an issue in or Think its inappropriate.\r\nPlease do reach us out.', 0);

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

CREATE TABLE `test` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `trig`
--

CREATE TABLE `trig` (
  `id` int(11) NOT NULL,
  `fid` varchar(50) NOT NULL,
  `action` varchar(50) NOT NULL,
  `timestamp` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `trig`
--

INSERT INTO `trig` (`id`, `fid`, `action`, `timestamp`) VALUES
(1, 'Real Time (Image Processing)', 'good', '2023-03-15 14:26:04'),
(2, 'RS', 'poor', '2023-03-15 14:26:05'),
(3, 'ML', 'Very Good', '2023-03-15 14:27:46');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `password`) VALUES
(6, 'prithviraj', 'prithvi456t@gmail.com', 'pbkdf2:sha256:260000$RPS9kWTEgZ0svY0W$5e223a2191b2e39e9d79371df18370662572ae2927b1bbb24a8f0035d916c59e');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`rid`);

--
-- Indexes for table `report`
--
ALTER TABLE `report`
  ADD PRIMARY KEY (`pid`);

--
-- Indexes for table `test`
--
ALTER TABLE `test`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `trig`
--
ALTER TABLE `trig`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `rid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `report`
--
ALTER TABLE `report`
  MODIFY `pid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `test`
--
ALTER TABLE `test`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `trig`
--
ALTER TABLE `trig`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
