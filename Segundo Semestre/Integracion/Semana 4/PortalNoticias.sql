-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Aug 19, 2022 at 12:35 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `PortalNoticias`
--

-- --------------------------------------------------------

--
-- Table structure for table `Comentarios`
--

CREATE TABLE `Comentarios` (
  `ID_Comentario` int(11) NOT NULL,
  `ID_Noticia` int(11) DEFAULT NULL,
  `Rut` int(11) DEFAULT NULL,
  `Comentario` varchar(100) DEFAULT NULL,
  `DateHour` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Noticia`
--

CREATE TABLE `Noticia` (
  `ID_Noticia` int(11) NOT NULL,
  `ID_Seccion` int(11) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Titulo` varchar(50) DEFAULT NULL,
  `Cuerpo` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Secciones`
--

CREATE TABLE `Secciones` (
  `ID_Seccion` int(11) NOT NULL,
  `Nombre` char(1) DEFAULT NULL,
  `Descripcion` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Usuario`
--

CREATE TABLE `Usuario` (
  `Rut` int(11) NOT NULL,
  `Nombre` char(20) DEFAULT NULL,
  `Primer_Apellido` char(25) DEFAULT NULL,
  `Edad` int(11) DEFAULT NULL,
  `Username` varchar(25) DEFAULT NULL,
  `Contrasena` varchar(25) DEFAULT NULL,
  `Admin` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Comentarios`
--
ALTER TABLE `Comentarios`
  ADD PRIMARY KEY (`ID_Comentario`),
  ADD KEY `ID_Noticia` (`ID_Noticia`),
  ADD KEY `ID_Usuario` (`Rut`);

--
-- Indexes for table `Noticia`
--
ALTER TABLE `Noticia`
  ADD PRIMARY KEY (`ID_Noticia`),
  ADD KEY `ID_Seccion` (`ID_Seccion`);

--
-- Indexes for table `Secciones`
--
ALTER TABLE `Secciones`
  ADD PRIMARY KEY (`ID_Seccion`);

--
-- Indexes for table `Usuario`
--
ALTER TABLE `Usuario`
  ADD PRIMARY KEY (`Rut`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Comentarios`
--
ALTER TABLE `Comentarios`
  ADD CONSTRAINT `Comentarios_ibfk_1` FOREIGN KEY (`ID_Noticia`) REFERENCES `Noticia` (`ID_Noticia`),
  ADD CONSTRAINT `Comentarios_ibfk_2` FOREIGN KEY (`Rut`) REFERENCES `Usuario` (`Rut`);

--
-- Constraints for table `Noticia`
--
ALTER TABLE `Noticia`
  ADD CONSTRAINT `Noticia_ibfk_1` FOREIGN KEY (`ID_Seccion`) REFERENCES `Secciones` (`ID_Seccion`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
