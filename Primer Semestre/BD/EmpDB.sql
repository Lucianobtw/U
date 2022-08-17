-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 26-06-2022 a las 21:21:47
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
-- Base de datos: `EmpDB`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `InsertNuevoEmp` (IN `NoEmpleado` INT, IN `Nombre` VARCHAR(20), IN `Apellido` VARCHAR(20), IN `FechaNacimiento` DATE, IN `Sexo` CHAR(20), IN `Sueldo` INT)  INSERT INTO empleados(NoEmpleado, Nombre, Apellido, FechaNacimiento, Sexo, Sueldo) 
VALUES (NoEmpleado, Nombre, Apellido, FechaNacimiento, Sexo, Sueldo)$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `SelectAll` ()  SELECT * FROM `empleados`$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `UpdateDescripcion` (IN `NumeroDeEmpleado` INT, IN `nuevadescripcion` VARCHAR(75))  UPDATE empleados
SET  descripcion = nuevadescripcion
WHERE NoEmpleado = NumeroDeEmpleado$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `UpdateSueldo` (IN `porcentaje` INT, IN `NumeroDeEmpleado` INT)  UPDATE empleados
SET  Sueldo = Sueldo + (Sueldo*porcentaje)/100
WHERE NoEmpleado = NumeroDeEmpleado$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `NoEmpleado` int NOT NULL,
  `Primer Apellido` char(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL,
  `Primer Nombre` char(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL,
  `FechaNacimiento` date DEFAULT NULL,
  `Sexo` enum('Femenino','Masculino') DEFAULT NULL,
  `Sueldo` int DEFAULT NULL,
  `Departamento` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL,
  `descripcion` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`NoEmpleado`, `Primer Apellido`, `Primer Nombre`, `FechaNacimiento`, `Sexo`, `Sueldo`, `Departamento`, `descripcion`) VALUES
(1, 'Perez', 'Juan', '1975-10-18', 'Masculino', 750000, 'Marketing', 'Rubio ojos café mediana estatura'),
(2, 'Brito', 'Alan', '1985-02-10', 'Masculino', 550000, 'Finanzas', 'mejor empleado'),
(3, 'Zurita', 'Juan Guillermo', '1945-12-15', 'Masculino', 624000, 'Control de Producció', 'moreno de ojos cafe'),
(4, 'Lege', 'Toge Eduardo', '1972-11-02', 'Masculino', 756850, 'Finanzas', 'tranquilo alto joven'),
(5, 'Ibieta', 'María Fernanda', '1969-09-04', 'Femenino', 687000, 'Control de Producció', 'morena de ojos azules'),
(6, 'Urquidi', 'Francisca', '1964-05-24', 'Femenino', 624000, 'Mantención', 'Rubia ojos café media estatura'),
(7, 'Hernandez', 'Hermes', '1967-02-02', 'Masculino', 750000, 'Informática', 'ojos café crespo inquieto'),
(8, 'Urbano', 'Paula Solange', '1954-01-09', 'Femenino', 350000, 'Mantención', 'Rubia ojos pardos alegre'),
(9, 'Abarzua', 'Alejandro Alfonso', '1972-05-29', 'Masculino', 378000, 'Publicidad y Marketing', 'ojos café alto inquieto'),
(10, 'Brettone', 'Fiorella Marieta', '1975-10-02', 'Femenino', 587000, 'Asesoría Legal', 'trigueña de ojos verdes azulados'),
(11, 'Cuming', 'Astor', '1959-04-03', 'Masculino', 780000, 'Ventas', NULL),
(12, 'Dubai', 'Alam', '1973-09-11', 'Masculino', 255000, 'Informática', NULL),
(13, 'Yutronik', 'Cristina', '1954-06-08', 'Femenino', 780000, 'Deportes y Recreació', 'Le gusta ir al gimnacio durante la semana.'),
(14, 'Eltit', 'Elisa', '1968-08-08', 'Femenino', 645000, 'Asesoría Legal', NULL),
(15, 'Who', 'Josep', '1960-02-15', 'Masculino', 1025000, 'Ventas', NULL),
(16, 'Fontanarosa', 'Natario', '1968-02-28', 'Masculino', 460000, 'Publicidad y Marketing', NULL),
(17, 'Vidals', 'Rebeca', '1965-10-12', 'Femenino', 698000, 'Finanzas', NULL),
(18, 'Gemma', 'Libera Maria', '1959-07-16', 'Femenino', 860000, 'Finanzas', 'taciturna buenamoza'),
(19, 'Tolle', 'Liucanio', '1972-04-09', 'Masculino', 745000, 'Ventas', 'camina rápido generalmente'),
(20, 'Justine', 'Paolo', '1945-12-08', 'Masculino', 895000, 'Mantención', NULL),
(21, 'Sabú', 'Arilton', '1963-12-04', 'Masculino', 960000, 'Asesoría Legal', 'extangero hace años '),
(22, 'Lacomtiu', 'Lucrecia', '1962-07-27', 'Femenino', 520000, 'Publicidad y Marketing', NULL),
(23, 'Spin', 'Roger', '1958-10-25', 'Masculino', 684000, 'Mantención', NULL),
(24, 'Moreira', 'Ivan Andres', '1966-04-18', 'Masculino', 150000, 'Deportes y Recreació', NULL),
(25, 'Ratziwilly', 'Lina Luna', '1965-09-19', 'Femenino', 597000, 'Ventas', 'deportista destacada nacional'),
(26, 'Noriega', 'Barbara Andrea', '1976-10-18', 'Femenino', 600000, 'Publicidad y Marketing', 'fuma esta en tratamiento'),
(27, 'Queiros', 'Victor', '1956-03-18', 'Masculino', 702000, 'Asesoría Legal', NULL),
(28, 'Ortuzar', 'Alejandra', '1966-11-10', 'Femenino', 450000, 'Publicidad y Marketing', NULL),
(29, 'Ubilla', 'Cecilia', '1960-11-25', 'Femenino', 580000, 'Ventas', NULL),
(30, 'Miller', 'Gunter', '1956-11-11', 'Masculino', 550000, 'Finanzas', NULL),
(31, 'Domdee', 'Aluska', '1962-01-18', 'Femenino', 350000, 'Ventas', NULL),
(32, 'Mulento', 'Pajar', '1975-08-10', 'Masculino', 760000, 'Ventas', NULL),
(33, 'Larkof', 'Lionertu', '1956-09-18', 'Masculino', 830000, 'Mantención', NULL),
(34, 'Hop', 'Carla', '1962-12-23', 'Femenino', 320000, 'Informática', NULL),
(35, 'Zarkis', 'Carmen Gloria', '1956-11-10', 'Femenino', 650000, 'Deportes y Recreació', NULL),
(36, 'Romel', 'Frank', '1966-11-11', 'Masculino', 576000, 'Asesoría Legal', NULL),
(37, 'Evermore', 'Eva Luna', '1952-04-08', 'Femenino', 656000, 'Publicidad y Marketing', NULL),
(38, 'Orpel', 'Ramon', '1965-07-27', 'Masculino', 860000, 'Ventas', NULL),
(39, 'Floriano', 'Julio Juan', '1976-05-28', 'Masculino', 330000, 'Ventas', NULL),
(40, 'Pirro', 'Cecilia', '1972-02-23', 'Femenino', 480000, 'Ventas', NULL),
(41, 'Rojas', 'Eduardina', '1962-06-08', 'Femenino', 356000, 'Publicidad y Marketing', NULL),
(42, 'Lucrosan', 'Orlando', '1975-07-27', 'Masculino', 860000, 'Control de Producció', NULL),
(43, 'NorteSur', 'Igor Juan', '1946-05-28', 'Masculino', 630000, 'Ventas', NULL),
(44, 'Roth', 'Anabella', '1952-12-23', 'Femenino', 420000, 'Ventas', NULL),
(45, 'Reno', 'Rodolfo', '1990-10-31', 'Masculino', 500000, 'Informática', 'Trabajo temporal con Santa Claus'),
(46, 'Perez-Urrutia', 'Victoria', '1965-04-05', 'Femenino', 485000, 'Ventas', 'alta delgada rubia'),
(47, 'Santibanes', 'Pedro', '1991-09-04', 'Masculino', 500000, 'Marketing', NULL),
(48, 'Perez', 'Luis', '1990-09-21', 'Masculino', 900000, 'Marketing', NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`NoEmpleado`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
