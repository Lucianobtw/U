CREATE PROCEDURE NewUser
(Rut INT, Nombre CHAR(20), Primer_Apellido CHAR(25), Edad INT, Username varchar(25), Password varchar(25))
INSERT INTO Usuario(Rut, Nombre, Primer_Apellido, Edad, Username, Password)
VALUES (Rut, Nombre, Primer_Apellido, Edad, Username, Password)
