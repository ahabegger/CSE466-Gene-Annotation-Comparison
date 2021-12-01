-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 01, 2021 at 04:14 PM
-- Server version: 5.7.33-0ubuntu0.16.04.1
-- PHP Version: 7.0.33-0ubuntu0.16.04.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hofmanln`
--

-- --------------------------------------------------------

--
-- Table structure for table `Transcripts`
--

CREATE TABLE `Transcripts` (
  `Chromosome` int(60) DEFAULT NULL,
  `Annotation_Provider` varchar(60) DEFAULT NULL,
  `Type` varchar(60) DEFAULT NULL,
  `Start_Position` int(60) DEFAULT NULL,
  `End_Position` int(60) DEFAULT NULL,
  `Dots` varchar(60) DEFAULT NULL,
  `Dash` varchar(60) DEFAULT NULL,
  `Number` varchar(60) DEFAULT NULL,
  `Transcript ID` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
