-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 02, 2021 at 02:43 AM
-- Server version: 5.7.33-0ubuntu0.16.04.1
-- PHP Version: 7.0.33-0ubuntu0.16.04.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `habeggaj`
--

-- --------------------------------------------------------

--
-- Table structure for table `GeneCategories`
--

CREATE TABLE `GeneCategories` (
  `ReleaseNo` int(11) DEFAULT NULL,
  `mRNA` int(11) DEFAULT NULL,
  `three_prime_UTR` int(11) DEFAULT NULL,
  `exon` int(11) DEFAULT NULL,
  `CDS` int(11) DEFAULT NULL,
  `five_prime_UTR` int(11) DEFAULT NULL,
  `biological_region` int(11) DEFAULT NULL,
  `ncRNA_gene` int(11) DEFAULT NULL,
  `lnc_RNA` int(11) DEFAULT NULL,
  `rRNA` int(11) DEFAULT NULL,
  `snoRNA` int(11) DEFAULT NULL,
  `pseudogene` int(11) DEFAULT NULL,
  `pseudogenic_transcript` int(11) DEFAULT NULL,
  `miRNA` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `GeneCategories`
--

INSERT INTO `GeneCategories` (`ReleaseNo`, `mRNA`, `three_prime_UTR`, `exon`, `CDS`, `five_prime_UTR`, `biological_region`, `ncRNA_gene`, `lnc_RNA`, `rRNA`, `snoRNA`, `pseudogene`, `pseudogenic_transcript`, `miRNA`) VALUES
(100, 1492, 1139, 17169, 15378, 1687, 2445, 160, 243, 81, 7, 4, 4, 7),
(104, 1492, 1139, 17169, 15378, 1687, 2445, 160, 243, 81, 7, 4, 4, 7);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
