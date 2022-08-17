CREATE TABLE `Courrier` (
  `CourrierID` int(20),
  `Nombre` varchar(20),
  `Tipo_de_Envio` varchar(30),
  `Transporte` varchar(20),
  `DireccionSucursal` varchar(50),
  PRIMARY KEY (`CourrierID`)
);

CREATE TABLE `Tienda` (
  `ShopID` int(20),
  `Nombre` varchar(25),
  `Ciudad` varchar(25),
  `Superficie(m²)` int(20),
  `Direccion` varchar(25),
  PRIMARY KEY (`ShopID`)
);

CREATE TABLE `Zapatillas` (
  `ProductID` int,
  `Modelo` varchar(20),
  `Stock` varchar(20),
  `Material` varchar(20),
  `Precio` int,
  `Talla(Chile)` varchar(15),
  PRIMARY KEY (`ProductID`)
);

CREATE TABLE `Cliente` (
  `Rut` int,
  `Nombre` varchar(20),
  `Apellidos` varchar(20),
  `email` varchar(30),
  `Dominio` varchar(20),
  `Direccion` varchar(25),
  PRIMARY KEY (`Rut`)
);

CREATE TABLE `Boleta` (
  `IDBoleta` int,
  `Rut` int,
  `ProductID` int,
  `ShopID` int,
  `CourrierID` int,
  `Fecha` date,
  `Total` int,
  PRIMARY KEY (`IDBoleta`),
  FOREIGN KEY (`Rut`) REFERENCES `Cliente`(`Rut`),
  FOREIGN KEY (`ProductID`) REFERENCES `Zapatillas`(`ProductID`),
  FOREIGN KEY (`CourrierID`) REFERENCES `Courrier`(`CourrierID`),
  FOREIGN KEY (`ShopID`) REFERENCES `Tienda`(`ShopID`)
);


