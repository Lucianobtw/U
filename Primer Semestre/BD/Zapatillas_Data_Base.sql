-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 26-06-2022 a las 21:22:02
-- Versión del servidor: 8.0.29-0ubuntu0.22.04.2
-- Versión de PHP: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `Zapatillas Data Base`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `InsertZapatilla` (IN `ProductID` INT, IN `Modelo` VARCHAR(20), IN `Stock` INT, IN `Material` VARCHAR(20), IN `Precio` INT, IN `Talla` VARCHAR(15))  INSERT INTO Zapatillas(ProductID, Modelo, Stock, Material, Precio, Talla) 
VALUES (ProductID, Modelo, Stock, Material, Precio, Talla)$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `SelectAll` ()  SELECT * FROM Zapatillas$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `UpdatePrecio` (`ProductID` INT, `Porcentaje` INT)  UPDATE Zapatillas
SET  Precio = Precio + (Precio*porcentaje)/100
WHERE ProductID = ProductID$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Boleta`
--

CREATE TABLE `Boleta` (
  `IDBoleta` int NOT NULL,
  `Rut` int DEFAULT NULL,
  `ProductID` int DEFAULT NULL,
  `ShopID` int DEFAULT NULL,
  `CourrierID` int DEFAULT NULL,
  `IDEnvio` int DEFAULT NULL,
  `Fecha` date DEFAULT NULL,
  `Total` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `Boleta`
--

INSERT INTO `Boleta` (`IDBoleta`, `Rut`, `ProductID`, `ShopID`, `CourrierID`, `IDEnvio`, `Fecha`, `Total`) VALUES
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
-- Estructura de tabla para la tabla `Cliente`
--

CREATE TABLE `Cliente` (
  `Rut` int NOT NULL,
  `Digito_Verificador` int DEFAULT NULL,
  `Primer_Nombre` varchar(20) DEFAULT NULL,
  `Segundo_Nombre` varchar(20) DEFAULT NULL,
  `Apellido_Paterno` varchar(20) DEFAULT NULL,
  `Apellido_Materno` varchar(20) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `Cliente`
--

INSERT INTO `Cliente` (`Rut`, `Digito_Verificador`, `Primer_Nombre`, `Segundo_Nombre`, `Apellido_Paterno`, `Apellido_Materno`, `email`) VALUES
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
-- Estructura de tabla para la tabla `Courrier`
--

CREATE TABLE `Courrier` (
  `CourrierID` int NOT NULL,
  `Nombre` varchar(20) DEFAULT NULL,
  `Direccion_Sucursa(calle)` varchar(25) DEFAULT NULL,
  `Numero_de_calle` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `Courrier`
--

INSERT INTO `Courrier` (`CourrierID`, `Nombre`, `Direccion_Sucursa(calle)`, `Numero_de_calle`) VALUES
(1, 'FedEX', 'Fco Bilbao', 190),
(2, 'DHL', 'San Martin', 501),
(3, 'Starken', 'Rodriguez', 97),
(4, 'Chilexpress', '18 de Septiembre', 1090),
(5, 'Correos de Chile', 'Prat', 852),
(6, 'ExpreSShip', 'Cordillera', 289);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Envio`
--

CREATE TABLE `Envio` (
  `IDEnvio` int NOT NULL,
  `Tipo_de_envio` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `Envio`
--

INSERT INTO `Envio` (`IDEnvio`, `Tipo_de_envio`) VALUES
(1, 'Reparto Exterior'),
(2, 'Reparto Local');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Tienda`
--

CREATE TABLE `Tienda` (
  `ShopID` int NOT NULL,
  `Nombre` varchar(25) DEFAULT NULL,
  `Ciudad` varchar(25) DEFAULT NULL,
  `Superficie` int DEFAULT NULL,
  `Direccion` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Numero_de_calle` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `Tienda`
--

INSERT INTO `Tienda` (`ShopID`, `Nombre`, `Ciudad`, `Superficie`, `Direccion`, `Numero_de_calle`) VALUES
(1, 'NikeStore', 'Santiago', 100, 'Fco Bilbao', 790),
(2, 'AdiShop', 'Temuco', 50, 'San Martin', 832),
(3, 'DCFLOW', 'Concepcion', 70, 'Rodriguez', 595),
(4, 'nBaSHOP', 'Valparaiso', 110, '18 de Septiembre', 367),
(5, 'NWStore', 'Valdivia', 55, 'Prat', 21),
(6, 'VansWW', 'Santiago', 55, 'Cordillera', 612);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Zapatillas`
--

CREATE TABLE `Zapatillas` (
  `ProductID` int NOT NULL,
  `Modelo` varchar(20) DEFAULT NULL,
  `Stock` varchar(20) DEFAULT NULL,
  `Material` varchar(20) DEFAULT NULL,
  `Precio` int DEFAULT NULL,
  `Talla` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `Zapatillas`
--

INSERT INTO `Zapatillas` (`ProductID`, `Modelo`, `Stock`, `Material`, `Precio`, `Talla`) VALUES
(1, 'Nike Air Force 1', '15', 'Sintetico', 90000, '42'),
(2, 'Adidas Valencia', '20', 'Cuero', 60000, '39'),
(3, 'DC Central M', '50', 'Gamusa', 55000, '43'),
(4, 'JORDAN R1 LOW', '15', 'Cuero', 109000, '41'),
(5, 'NW550', '30', 'Cuerina', 49000, '40'),
(6, 'Nike DUNK LOW', '15', 'Cuero', 99000, '43'),
(7, 'Adidas Adizero', '20', 'Sintetico', 60000, '39'),
(8, 'DC SK2', '50', 'Gamusa', 70000, '39'),
(9, 'JORDAN AIR', '15', 'Cuero', 120000, '41'),
(10, 'Ultrarange', '100', 'Malla', 59000, '42'),
(11, 'Nike DUNK LOW', '32', 'Cuero', 62074, '42'),
(12, 'Nike CR7 2.0', '74', 'Sintetico', 69224, '40'),
(13, 'Nike WalkMan', '80', 'Cuerina', 106408, '41'),
(14, 'Nike RUN PRO', '56', 'Malla', 103439, '40'),
(15, 'Nike CR7', '83', 'Sintetico', 90814, '45'),
(16, 'Nike Air Force 2', '76', 'Cuero', 110849, '44'),
(17, 'Nike Casual 02', '83', 'Gamuza', 83613, '43'),
(18, 'Nike Speed 03', '28', 'Cuero', 107608, '45'),
(19, 'Nike Walk 02', '96', 'Sintetico', 109373, '41'),
(20, 'Nike MR1', '28', 'Malla', 89354, '40'),
(21, 'Zapatilla T7', '100', 'Cuero', 55000, '43');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `Boleta`
--
ALTER TABLE `Boleta`
  ADD PRIMARY KEY (`IDBoleta`),
  ADD KEY `Rut` (`Rut`),
  ADD KEY `ShopID` (`ShopID`),
  ADD KEY `CourrierID` (`CourrierID`),
  ADD KEY `ProductID` (`ProductID`),
  ADD KEY `IDEnvio` (`IDEnvio`);

--
-- Indices de la tabla `Cliente`
--
ALTER TABLE `Cliente`
  ADD PRIMARY KEY (`Rut`);

--
-- Indices de la tabla `Courrier`
--
ALTER TABLE `Courrier`
  ADD PRIMARY KEY (`CourrierID`);

--
-- Indices de la tabla `Envio`
--
ALTER TABLE `Envio`
  ADD PRIMARY KEY (`IDEnvio`);

--
-- Indices de la tabla `Tienda`
--
ALTER TABLE `Tienda`
  ADD PRIMARY KEY (`ShopID`);

--
-- Indices de la tabla `Zapatillas`
--
ALTER TABLE `Zapatillas`
  ADD PRIMARY KEY (`ProductID`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `Boleta`
--
ALTER TABLE `Boleta`
  ADD CONSTRAINT `Boleta_ibfk_1` FOREIGN KEY (`Rut`) REFERENCES `Cliente` (`Rut`),
  ADD CONSTRAINT `Boleta_ibfk_2` FOREIGN KEY (`ShopID`) REFERENCES `Tienda` (`ShopID`),
  ADD CONSTRAINT `Boleta_ibfk_4` FOREIGN KEY (`CourrierID`) REFERENCES `Courrier` (`CourrierID`),
  ADD CONSTRAINT `Boleta_ibfk_5` FOREIGN KEY (`ProductID`) REFERENCES `Zapatillas` (`ProductID`),
  ADD CONSTRAINT `Boleta_ibfk_6` FOREIGN KEY (`IDEnvio`) REFERENCES `Envio` (`IDEnvio`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
