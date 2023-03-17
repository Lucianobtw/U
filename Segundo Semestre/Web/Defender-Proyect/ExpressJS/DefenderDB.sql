-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 192.168.4.20
-- Tiempo de generación: 06-01-2023 a las 15:30:34
-- Versión del servidor: 10.6.10-MariaDB
-- Versión de PHP: 7.4.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `A2022_lrevillod`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contacto`
--

CREATE TABLE `contacto` (
  `ID` int(11) NOT NULL,
  `Primer_Nombre` varchar(25) NOT NULL,
  `Primer_Apellido` varchar(25) NOT NULL,
  `email` varchar(50) NOT NULL,
  `Asunto` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `contacto`
--

INSERT INTO `contacto` (`ID`, `Primer_Nombre`, `Primer_Apellido`, `email`, `Asunto`) VALUES
(182, 'Luciano ', 'Revillod', 'lrevillod2022@alu.uct.cl', 'Hola esto es ExpressJS'),
(184, 'Nicolas', 'Ketterer', 'nketterer@gmail.com', 'Hola'),
(190, 'Mauricio', 'Aguilera', 'maguilera@alu.com', 'Hola soy mauricio y me gustaria decir que su producto es el mejor, felicitaciones y sigan asi'),
(191, 'Luciano', 'Revillod', 'lrevillod2022@alu.uct.cl', 'Hola soy mauricio y me gustaria decir que su producto es el mejor, felicitaciones y sigan asi'),
(196, 'Evaluacion', 'IV', 'soy@la.evaluacion', 'Test evaluacion');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Nosotros`
--

CREATE TABLE `Nosotros` (
  `ID` int(8) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `Descripcion` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `Nosotros`
--

INSERT INTO `Nosotros` (`ID`, `Nombre`, `email`, `Descripcion`) VALUES
(1, 'Luciano Ignacio Revillod Jerez', 'lrevillod2022@alu.uct.cl', 'Estudiante de Ingenieria civil informatica de la universidad Catolica de Temuco'),
(2, 'Nicolas Valenzuela Maliqueo', 'nvalenzuela2022@alu.uct.cl', 'Estudiante de Ingenieria civil informatica de la universidad Catolica de Temuco');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sessions`
--

CREATE TABLE `sessions` (
  `session_id` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `expires` int(11) UNSIGNED NOT NULL,
  `data` mediumtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `sessions`
--

INSERT INTO `sessions` (`session_id`, `expires`, `data`) VALUES
('fIOKU7FXqHqyNJicXv7GKWgK270Mll_M', 1830698277, '{\"cookie\":{\"originalMaxAge\":null,\"expires\":null,\"httpOnly\":true,\"path\":\"/\"},\"user\":\"MrRevillod\",\"Admin\":1}'),
('fg7DjxB8AbJTbk7Jnf-n8YPpApCSCTIy', 1830698316, '{\"cookie\":{\"originalMaxAge\":null,\"expires\":null,\"httpOnly\":true,\"path\":\"/\"},\"user\":\"MrRevillod\",\"Admin\":1}'),
('fue0M5k2QJmAgrWqNbiaWZB1zYbu3Zn_', 1830698296, '{\"cookie\":{\"originalMaxAge\":null,\"expires\":null,\"httpOnly\":true,\"path\":\"/\"},\"user\":\"NIcoVZ\",\"Admin\":0}');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Usuarios`
--

CREATE TABLE `Usuarios` (
  `RUT` int(11) NOT NULL,
  `Username` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci NOT NULL,
  `email` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci NOT NULL,
  `password` varchar(8000) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci NOT NULL,
  `Admin` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `Usuarios`
--

INSERT INTO `Usuarios` (`RUT`, `Username`, `email`, `password`, `Admin`) VALUES
(10987123, 'User', 'user@user.com', 'd404559f602eab6fd602ac7680dacbfaadd13630335e951f097af3900e9de176b6db28512f2e000b9d04fba5133e8b1c6e8df59db3a8ab9d60be4b97cc9e81db', 0),
(12345123, 'Rev', 'rev@rev.com', 'd404559f602eab6fd602ac7680dacbfaadd13630335e951f097af3900e9de176b6db28512f2e000b9d04fba5133e8b1c6e8df59db3a8ab9d60be4b97cc9e81db', 0),
(21395308, 'MrRevillod', 'lrevillod2022@alu.uct.cl', 'bf2121ff91f6981ec3563732c5449209d504b6036a4d924e71dd4262d4eb770554f1641a20d72cf3b02cc8e914fc1ec36ef8a36b9e4092db0340b664cee6648f', 1),
(21397812, 'laksjad', 'alkjsd@lsdk.c', '3043aa4a83b0934982956a90828140cb834869135b5f294938865de12e036de440a330e1e8529bec15ddd59f18d1161a97bfec110d2622680f2c714a737d7061', 0),
(21568322, 'NIcoVZ', 'nvalenzuela2022@alu.uct.cl', 'bf2121ff91f6981ec3563732c5449209d504b6036a4d924e71dd4262d4eb770554f1641a20d72cf3b02cc8e914fc1ec36ef8a36b9e4092db0340b664cee6648f', 0),
(30123456, 'Pedrito', 'pedro@pedro.com', 'd404559f602eab6fd602ac7680dacbfaadd13630335e951f097af3900e9de176b6db28512f2e000b9d04fba5133e8b1c6e8df59db3a8ab9d60be4b97cc9e81db', 0),
(31456123, 'Cris', 'cri@juan.com', 'd404559f602eab6fd602ac7680dacbfaadd13630335e951f097af3900e9de176b6db28512f2e000b9d04fba5133e8b1c6e8df59db3a8ab9d60be4b97cc9e81db', 0),
(32987123, 'Oscar', 'me@me.me', 'd404559f602eab6fd602ac7680dacbfaadd13630335e951f097af3900e9de176b6db28512f2e000b9d04fba5133e8b1c6e8df59db3a8ab9d60be4b97cc9e81db', 0),
(40123906, 'OscarM', 'mella@god.com', 'd404559f602eab6fd602ac7680dacbfaadd13630335e951f097af3900e9de176b6db28512f2e000b9d04fba5133e8b1c6e8df59db3a8ab9d60be4b97cc9e81db', 0),
(43678678, 'Csslaj', 'cs@ja.com', 'd404559f602eab6fd602ac7680dacbfaadd13630335e951f097af3900e9de176b6db28512f2e000b9d04fba5133e8b1c6e8df59db3a8ab9d60be4b97cc9e81db', 0),
(67213345, 'posssd', 'ssldk@skd.com', 'd404559f602eab6fd602ac7680dacbfaadd13630335e951f097af3900e9de176b6db28512f2e000b9d04fba5133e8b1c6e8df59db3a8ab9d60be4b97cc9e81db', 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `contacto`
--
ALTER TABLE `contacto`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `Nosotros`
--
ALTER TABLE `Nosotros`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `sessions`
--
ALTER TABLE `sessions`
  ADD PRIMARY KEY (`session_id`);

--
-- Indices de la tabla `Usuarios`
--
ALTER TABLE `Usuarios`
  ADD PRIMARY KEY (`RUT`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `contacto`
--
ALTER TABLE `contacto`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=198;
COMMIT;