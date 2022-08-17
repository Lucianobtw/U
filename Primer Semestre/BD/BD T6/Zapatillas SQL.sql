CREATE TABLE `Transporte` (
 `IDEnvio` int,
 `Tipo_de_envio` varchar(30),
 PRIMARY KEY (`IDEnvio`)
);

CREATE TABLE `Courrier` (
 `CourrierID` int(20),
 `Nombre` varchar(20),
 `Direccion_Sucursa(calle)` varchar(25),
 `Numero_de_calle` int,
 PRIMARY KEY (`CourrierID`)
);

CREATE TABLE `Cliente` (
 `Rut` int,
 `Digito_Verificador` int(1),
 `Primer_Nombre` varchar(20),
 `Segundo_Nombre` varchar(20),
 `Apellido_Paterno` varchar(20),
 `Apellido_Materno` varchar(20),
 `email` varchar(30),
 PRIMARY KEY (`Rut`)
);

CREATE TABLE `Tienda` (
 `ShopID` int(20),
 `Nombre` varchar(25),
 `Ciudad` varchar(25),
 `Superficie(metros)` int,
 `Direccion (Calle)` varchar(25),
 `Numero_de_calle` int,
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

CREATE TABLE `Boleta` (
 `IDBoleta` int,
 `Rut` int,
 `ProductID` int,
 `ShopID` int,
 `CourrierID` int,
 `IDEnvio` int,
 `Fecha` date,
 `Total` int,
 PRIMARY KEY (`IDBoleta`),
 FOREIGN KEY (`Rut`) REFERENCES `Cliente`(`Rut`),
 FOREIGN KEY (`ShopID`) REFERENCES `Tienda`(`ShopID`),
 FOREIGN KEY (`IDEnvio`) REFERENCES `Transporte`(`IDEnvio`),
 FOREIGN KEY (`CourrierID`) REFERENCES `Courrier`(`CourrierID`),
 FOREIGN KEY (`ProductID`) REFERENCES `Zapatillas`(`ProductID`)
);


INSERT INTO `Boleta`(`IDBoleta`, `Rut`, `ProductID`, `ShopID`, `CourrierID`, `IDEnvio`, `Total`) VALUES

(11,21444971,11, 1 , 1 , 1 ,62074),
(12,20214796,12, 1 , 1 , 2 ,69224),
(13,20539748,13 , 1 , 1 , 2 ,106408),
(14,20446359,14 , 1 , 1 , 2 ,103439),
(15,21962969,15 , 1 , 1 , 2 ,90814),
(16,21037903,16 , 1 , 1 , 1 ,110849),
(17,20096300,17 , 1 , 1 , 1 ,83613 ),
(18,21522471,18 , 1 , 1 , 1 ,107608),
(19,21689541,19 , 1 , 1 , 2 ,109373),
(20,20023608,20 , 1 , 1 , 2 ,89354);




INSERT INTO `Cliente`(`Rut`, `Digito_Verificador`, `Primer_Nombre`, `Segundo_Nombre`, `Apellido_Paterno`, `Apellido_Materno`, `email`) VALUES 

(21444971,3,'Martin','Ignacio','Perez','Martinez','mim@gmail.com')
(20214796,2,'Olga','Del carmen','Lagos','jimenez','Olgalagos@outlook.com')
(20539748,5,'Ignacio','Sebastian','Jimenez','Henriquez','ijhen@gmail.com')
(20446359,3,'Joaquin','Rumualdo','Prieto','San Martin','Joaco@gmail.com')
(21962969,2,'Guisela','Maria','Ordones','Fernandez','gigi@gmail.com')
(21037903,1,'Fermin','Aldredo','Vial','Henriquez','FernanV@gmail.com')
(20096300,2,'Matias','Alejandro','Garcia','Bustamante','Matibus@gmail.com')
(21522471,7,'Nicolas','Matias','Beltran','Lopez','nicogod@gmail.com')
(21689541,0,'Eliana','Laura','Fernandez','Paredes','Efer@gmail.com')
(20023608,8,'Daniela','Andrea','Perez','Munoz','DaniAndrea@gmail.com')


INSERT INTO `Zapatillas`(`ProductID`, `Modelo`, `Stock`, `Material`, `Precio`, `Talla`) VALUES

( 11 ,'Nike DUNK LOW', 32 ,'Cuero', 62074 , 42 ),
( 12 ,'Nike CR7 2.0', 74 ,'Sintetico', 69224 , 40 ),
( 13 ,'Nike WalkMan', 80 ,'Cuerina', 106408 , 41 ),
( 14 ,'Nike RUN PRO', 56 ,'Malla', 103439 , 40 ),
( 15 ,'Nike CR7', 83 ,'Sintetico', 90814 , 45 ),
( 16 ,'Air Force 2', 76 ,'Cuero', 110849 , 44 ),
( 17 ,'Nike Casual 02', 83 ,'Gamuza', 83613 , 43 ),
( 18 ,'Nike Speed 03', 28 ,'Cuero', 107608 , 45 ),
( 19 ,'Nike Walk 02', 96 ,'Sintetico', 109373 , 41 ),
( 20 ,'Nike MR1', 28 ,'Malla', 89354 , 40 );