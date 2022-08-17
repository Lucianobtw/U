-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-06-2022 a las 02:07:21
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `zapatillasdb`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `InsertZapatilla` (IN `ProductID` INT, IN `Modelo` VARCHAR(20), IN `Stock` INT, IN `Material` VARCHAR(20), IN `Precio` INT, IN `Talla` VARCHAR(15))   INSERT INTO zapatillas(ProductID, Modelo, Stock, Material, Precio, Talla) 
VALUES (ProductID, Modelo, Stock, Material, Precio, Talla)$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `SelectAll` ()   SELECT * FROM Zapatillas$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `UpdatePrecio` (IN `IDproducto` INT, IN `porcentaje` INT)   UPDATE zapatillas
SET  Precio = Precio + (Precio*porcentaje)/100
WHERE ProductID = IDproducto$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `boleta`
--

CREATE TABLE `boleta` (
  `IDBoleta` int(11) NOT NULL,
  `Rut` int(11) DEFAULT NULL,
  `ProductID` int(11) DEFAULT NULL,
  `ShopID` int(11) DEFAULT NULL,
  `CourrierID` int(11) DEFAULT NULL,
  `IDEnvio` int(11) DEFAULT NULL,
  `Fecha` date DEFAULT NULL,
  `Total` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `boleta`
--

INSERT INTO `boleta` (`IDBoleta`, `Rut`, `ProductID`, `ShopID`, `CourrierID`, `IDEnvio`, `Fecha`, `Total`) VALUES
(1, 21395308, 1, 1, 1, 1, '2022-02-10', 90000),
(2, 20456202, 2, 2, 2, 2, '2021-08-10', 60000),
(3, 18178275, 3, 3, 3, 1, '2022-05-20', 55000),
(4, 20432126, 4, 4, 4, 2, '2022-06-06', 109000),
(5, 21508503, 5, 5, 5, 1, '2021-12-22', 49000),
(6, 21395208, 6, 1, 1, 2, '2021-10-24', 99000),
(7, 20456290, 7, 2, 2, 1, '2022-01-12', 60000),
(8, 18178234, 8, 3, 3, 2, '2021-11-14', 70000),
(9, 20432426, 9, 4, 4, 1, '2022-04-20', 120000),
(10, 21504203, 10, 6, 6, 2, '2022-05-21', 59000),
(11, 21444971, 11, 1, 1, 1, NULL, 62074),
(12, 20214796, 12, 1, 1, 2, NULL, 69224),
(13, 20539748, 13, 1, 1, 2, NULL, 106408),
(14, 20446359, 14, 1, 1, 2, NULL, 103439),
(15, 21962969, 15, 1, 1, 2, NULL, 90814),
(16, 21037903, 16, 1, 1, 1, NULL, 110849),
(17, 20096300, 17, 1, 1, 1, NULL, 83613),
(18, 21522471, 18, 1, 1, 1, NULL, 107608),
(19, 21689541, 19, 1, 1, 2, NULL, 109373),
(20, 20023608, 20, 1, 1, 2, NULL, 89354);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `Rut` int(11) NOT NULL,
  `Digito_Verificador` int(11) DEFAULT NULL,
  `Primer_Nombre` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Segundo_Nombre` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Apellido_Paterno` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Apellido_Materno` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `email` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`Rut`, `Digito_Verificador`, `Primer_Nombre`, `Segundo_Nombre`, `Apellido_Paterno`, `Apellido_Materno`, `email`) VALUES
(18178234, 6, 'Luciano', 'Javier', 'Ramirez', 'Jimenez', 'lucianor@outlook.com'),
(18178275, 6, 'Ignacia', 'Belen', 'Bastias', 'Perez', 'ibastias@outlook.es'),
(20023608, 8, 'Daniela', 'Andrea', 'Perez', 'Munoz', 'DaniAndrea@gmail.com'),
(20096300, 2, 'Matias', 'Alejandro', 'Garcia', 'Bustamante', 'Matibus@gmail.com'),
(20214796, 2, 'Olga', 'Del carmen', 'Lagos', 'jimenez', 'Olgalagos@outlook.com'),
(20432126, 5, 'Daniel', 'Ignacio', 'Henriquez', 'Estrada', 'dhenriquez@gmail.com'),
(20432426, 5, 'Daniela', 'Antonia', 'Weber', 'Monsalves', 'dweber@gmail.com'),
(20446359, 3, 'Joaquin', 'Rumualdo', 'Prieto', 'San Martin', 'Joaco@gmail.com'),
(20456202, 6, 'Javier', 'Matias', 'Jimenez', 'Salas', 'jjimenez@gmail.com'),
(20456290, 6, 'Kristian', 'Rafael', 'Henriquez', 'Zapata', 'khenriquez@gmail.com'),
(20539748, 5, 'Ignacio', 'Sebastian', 'Jimenez', 'Henriquez', 'ijhen@gmail.com'),
(21037903, 1, 'Fermin', 'Aldredo', 'Vial', 'Henriquez', 'FernanV@gmail.com'),
(21395208, 7, 'Jaime', 'Luis', 'Rodriguez', 'Perez', 'jrodriguez2022@alu.uct.cl'),
(21395308, 7, 'Luciano', 'Ignacio', 'Revillod', 'Jerez', 'lrevillod2022@alu.uct.cl'),
(21444971, 3, 'Martin', 'Ignacio', 'Perez', 'Martinez', 'mim@gmail.com'),
(21504203, 8, 'Peter', 'Angel', 'Estrada', 'Rios', 'pestrada@yahoo.es'),
(21508503, 8, 'Pedro', 'Javier', 'Lopez', 'Estrada', 'pestrada@yahoo.es'),
(21522471, 7, 'Nicolas', 'Matias', 'Beltran', 'Lopez', 'nicogod@gmail.com'),
(21689541, 0, 'Eliana', 'Laura', 'Fernandez', 'Paredes', 'Efer@gmail.com'),
(21962969, 2, 'Guisela', 'Maria', 'Ordones', 'Fernandez', 'gigi@gmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `courrier`
--

CREATE TABLE `courrier` (
  `CourrierID` int(11) NOT NULL,
  `Nombre` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Direccion_Sucursa(calle)` varchar(25) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Numero_de_calle` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `courrier`
--

INSERT INTO `courrier` (`CourrierID`, `Nombre`, `Direccion_Sucursa(calle)`, `Numero_de_calle`) VALUES
(1, 'FedEX', 'Fco Bilbao', 190),
(2, 'DHL', 'San Martin', 501),
(3, 'Starken', 'Rodriguez', 97),
(4, 'Chilexpress', '18 de Septiembre', 1090),
(5, 'Correos de Chile', 'Prat', 852),
(6, 'ExpreSShip', 'Cordillera', 289);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `envio`
--

CREATE TABLE `envio` (
  `IDEnvio` int(11) NOT NULL,
  `Tipo_de_envio` varchar(25) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `envio`
--

INSERT INTO `envio` (`IDEnvio`, `Tipo_de_envio`) VALUES
(1, 'Reparto Exterior'),
(2, 'Reparto Local');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `temp_precio_update`
--

CREATE TABLE `temp_precio_update` (
  `logID` int(11) NOT NULL,
  `ProductID` int(11) NOT NULL,
  `OldPrecio` int(11) NOT NULL,
  `NewPrecio` int(11) NOT NULL,
  `Fecha_Hora` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `temp_precio_update`
--

INSERT INTO `temp_precio_update` (`logID`, `ProductID`, `OldPrecio`, `NewPrecio`, `Fecha_Hora`) VALUES
(1, 4, 375392, 379146, '2022-06-28 19:52:57'),
(2, 19, 376678, 414346, '2022-06-28 20:12:49'),
(3, 21, 189419, 208361, '2022-06-28 20:36:50'),
(4, 20, 307733, 461600, '2022-06-28 23:03:52'),
(5, 19, 414346, 621519, '2022-06-28 23:31:58'),
(6, 26, 50000, 50000, '2022-06-29 05:12:18'),
(7, 27, 50000, 50000, '2022-06-29 05:12:36'),
(8, 25, 50000, 50000, '2022-06-29 05:12:48'),
(9, 26, 50000, 55000, '2022-06-29 05:13:48'),
(10, 28, 50000, 57500, '2022-06-29 05:18:31'),
(11, 29, 20000, 30000, '2022-06-29 06:09:11'),
(12, 30, 50000, 75000, '2022-06-29 06:29:40'),
(13, 31, 50000, 75000, '2022-06-29 06:50:50'),
(14, 32, 50000, 75000, '2022-06-29 08:59:03'),
(15, 33, 20000, 22000, '2022-06-29 09:01:03'),
(16, 34, 10000, 15000, '2022-06-29 09:12:39'),
(17, 35, 50000, 75000, '2022-06-29 09:14:07'),
(18, 36, 30000, 33000, '2022-06-29 10:34:25'),
(19, 37, 20000, 26000, '2022-06-29 10:35:51'),
(20, 41, 50000, 55000, '2022-06-29 18:37:44'),
(21, 42, 20000, 30000, '2022-06-29 18:39:40');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `temp_zapatillas_insert`
--

CREATE TABLE `temp_zapatillas_insert` (
  `logID` int(11) NOT NULL,
  `ProductID` int(11) NOT NULL,
  `Stock` int(11) NOT NULL,
  `Fecha_Hora` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `temp_zapatillas_insert`
--

INSERT INTO `temp_zapatillas_insert` (`logID`, `ProductID`, `Stock`, `Fecha_Hora`) VALUES
(1, 22, 99, '2022-06-28 14:18:01'),
(2, 23, 100, '2022-06-28 14:27:08'),
(3, 24, 80, '2022-06-28 21:29:10'),
(6, 25, 100, '2022-06-28 23:42:31'),
(7, 27, 100, '2022-06-28 23:54:01'),
(8, 26, 100, '2022-06-29 05:11:44'),
(9, 28, 100, '2022-06-29 05:18:04'),
(10, 29, 50, '2022-06-29 06:08:26'),
(11, 30, 100, '2022-06-29 06:29:10'),
(12, 31, 100, '2022-06-29 06:50:04'),
(13, 32, 100, '2022-06-29 08:57:11'),
(14, 33, 100, '2022-06-29 09:00:21'),
(15, 34, 100, '2022-06-29 09:10:44'),
(16, 35, 100, '2022-06-29 09:13:43'),
(17, 36, 100, '2022-06-29 10:32:59'),
(18, 37, 100, '2022-06-29 10:35:20'),
(19, 38, 60, '2022-06-29 17:54:15'),
(20, 39, 100, '2022-06-29 17:54:59'),
(21, 40, 100, '2022-06-29 18:19:57'),
(22, 41, 70, '2022-06-29 18:36:18'),
(23, 42, 100, '2022-06-29 18:38:59');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tienda`
--

CREATE TABLE `tienda` (
  `ShopID` int(11) NOT NULL,
  `Nombre` varchar(25) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Ciudad` varchar(25) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Superficie` int(11) DEFAULT NULL,
  `Direccion` varchar(25) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Numero_de_calle` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `tienda`
--

INSERT INTO `tienda` (`ShopID`, `Nombre`, `Ciudad`, `Superficie`, `Direccion`, `Numero_de_calle`) VALUES
(1, 'NikeStore', 'Santiago', 100, 'Fco Bilbao', 790),
(2, 'AdiShop', 'Temuco', 50, 'San Martin', 832),
(3, 'DCFLOW', 'Concepcion', 70, 'Rodriguez', 595),
(4, 'nBaSHOP', 'Valparaiso', 110, '18 de Septiembre', 367),
(5, 'NWStore', 'Valdivia', 55, 'Prat', 21),
(6, 'VansWW', 'Santiago', 55, 'Cordillera', 612);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `zapatillas`
--

CREATE TABLE `zapatillas` (
  `ProductID` int(11) NOT NULL,
  `Modelo` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Stock` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Material` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Precio` int(11) DEFAULT NULL,
  `Talla` varchar(15) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `zapatillas`
--

INSERT INTO `zapatillas` (`ProductID`, `Modelo`, `Stock`, `Material`, `Precio`, `Talla`) VALUES
(1, 'Nike Air Force 1', '15', 'Sintetico', 309957, '42'),
(2, 'Adidas Valencia', '20', 'Cuero', 206638, '39'),
(3, 'DC Central M', '50', 'Gamusa', 189419, '43'),
(4, 'JORDAN R1 LOW', '15', 'Cuero', 379146, '41'),
(5, 'NW550', '30', 'Cuerina', 168754, '40'),
(6, 'Nike DUNK LOW', '15', 'Cuero', 340953, '43'),
(7, 'Adidas Adizero', '20', 'Sintetico', 206638, '39'),
(8, 'DC SK2', '50', 'Gamusa', 241078, '39'),
(9, 'JORDAN AIR', '15', 'Cuero', 413276, '41'),
(10, 'Ultrarange', '100', 'Malla', 207259, '42'),
(11, 'Nike DUNK LOW', '32', 'Cuero', 213782, '42'),
(12, 'Nike CR7 2.0', '74', 'Sintetico', 238404, '40'),
(13, 'Nike WalkMan', '80', 'Cuerina', 366466, '41'),
(14, 'Nike RUN PRO', '56', 'Malla', 356241, '40'),
(15, 'Nike CR7', '83', 'Sintetico', 312761, '45'),
(16, 'Nike Air Force 2', '76', 'Cuero', 381761, '44'),
(17, 'Nike Casual 02', '83', 'Gamuza', 287961, '43'),
(18, 'Nike Speed 03', '28', 'Cuero', 370598, '45'),
(19, 'Nike Walk 02', '96', 'Sintetico', 621519, '41'),
(20, 'Nike MR1', '28', 'Malla', 461600, '40'),
(21, 'Zapatilla T7', '100', 'Cuero', 208361, '43'),
(22, 'Zapatilla Act7', '99', 'Cuero', 58514, '42'),
(23, 'Zapatilla Act77', '100', 'Sintetico', 172199, '42'),
(24, 'TestWeb', '80', 'Cuero', 50000, '42'),
(25, 'zapatillatestin', '100', '1', 50000, '40'),
(26, 'zapatillatestinsert', '100', 'Cuero', 55000, '40'),
(27, 'zapatillatestinsert1', '100', 'Cuero', 50000, '45'),
(28, 'Insertestfinal', '100', 'Sintetico', 57500, '45'),
(29, 'Nike09', '50', 'Malla', 30000, '43'),
(30, 'testpaginaweb1', '100', 'Cuero', 75000, '40'),
(31, 'TEST1', '100', 'Cuero', 75000, '43'),
(32, 'video', '100', 'Cuero', 75000, '40'),
(33, 'video2', '100', 'Cuero', 22000, '41'),
(34, 'videotest1', '100', 'Sintetico', 15000, '42'),
(35, 'videotest3', '100', 'Malla', 75000, '42'),
(36, 'videofinal', '100', 'Sintetico', 33000, '42'),
(37, 'finzapatilla', '100', 'Sintetico', 26000, '41'),
(38, 'nike10', '60', 'Cuero', 50000, '42'),
(39, 'nike 11', '100', 'Malla', 20000, '44'),
(40, 'Zapatilla40', '100', 'Sintetico', 100000, '42'),
(41, 'Rebook1', '70', 'Cuero', 55000, '43'),
(42, 'Rebook2', '100', 'Malla', 30000, '42');

--
-- Disparadores `zapatillas`
--
DELIMITER $$
CREATE TRIGGER `Insert_Zapatilla_T` AFTER INSERT ON `zapatillas` FOR EACH ROW INSERT INTO temp_zapatillas_Insert (logID, ProductID, Stock, Fecha_Hora)
VALUES (logID,new.ProductID,new.Stock, now())
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `Update_Precio_T` BEFORE UPDATE ON `zapatillas` FOR EACH ROW INSERT INTO temp_precio_update(logID, ProductID, OldPrecio, NewPrecio, Fecha_Hora)
VALUES (logID, new.ProductID, old.Precio, new.Precio, now())
$$
DELIMITER ;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `boleta`
--
ALTER TABLE `boleta`
  ADD PRIMARY KEY (`IDBoleta`),
  ADD KEY `Rut` (`Rut`),
  ADD KEY `ShopID` (`ShopID`),
  ADD KEY `CourrierID` (`CourrierID`),
  ADD KEY `ProductID` (`ProductID`),
  ADD KEY `IDEnvio` (`IDEnvio`);

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`Rut`);

--
-- Indices de la tabla `courrier`
--
ALTER TABLE `courrier`
  ADD PRIMARY KEY (`CourrierID`);

--
-- Indices de la tabla `envio`
--
ALTER TABLE `envio`
  ADD PRIMARY KEY (`IDEnvio`);

--
-- Indices de la tabla `temp_precio_update`
--
ALTER TABLE `temp_precio_update`
  ADD PRIMARY KEY (`logID`);

--
-- Indices de la tabla `temp_zapatillas_insert`
--
ALTER TABLE `temp_zapatillas_insert`
  ADD PRIMARY KEY (`logID`);

--
-- Indices de la tabla `tienda`
--
ALTER TABLE `tienda`
  ADD PRIMARY KEY (`ShopID`);

--
-- Indices de la tabla `zapatillas`
--
ALTER TABLE `zapatillas`
  ADD PRIMARY KEY (`ProductID`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `temp_precio_update`
--
ALTER TABLE `temp_precio_update`
  MODIFY `logID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `temp_zapatillas_insert`
--
ALTER TABLE `temp_zapatillas_insert`
  MODIFY `logID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `boleta`
--
ALTER TABLE `boleta`
  ADD CONSTRAINT `Boleta_ibfk_1` FOREIGN KEY (`Rut`) REFERENCES `cliente` (`Rut`),
  ADD CONSTRAINT `Boleta_ibfk_2` FOREIGN KEY (`ShopID`) REFERENCES `tienda` (`ShopID`),
  ADD CONSTRAINT `Boleta_ibfk_4` FOREIGN KEY (`CourrierID`) REFERENCES `courrier` (`CourrierID`),
  ADD CONSTRAINT `Boleta_ibfk_5` FOREIGN KEY (`ProductID`) REFERENCES `zapatillas` (`ProductID`),
  ADD CONSTRAINT `Boleta_ibfk_6` FOREIGN KEY (`IDEnvio`) REFERENCES `envio` (`IDEnvio`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
