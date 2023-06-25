CREATE TABLE `tb_cat_rol` (
  `id_rol` int NOT NULL,
  `nombre_rol` varchar (100) NOT NULL,
) --Administrador, usuario

INSERT INTO tb_cat_rol (nombre_rol) 
VALUES('Administrador', 'Usuario' 
)

CREATE TABLE `tb_cat_genero` (
  `id_genero` int NOT NULL,
  `nombre_genero` varchar (100) NOT NULL,
) --Hombre, Mujer, Otro

INSERT INTO tb_cat_genero (nombre_genero) 
VALUES('Hombre', 'Mujer', 'Otro' 
)


CREATE TABLE `tb_persona` (
  `id_paciente` int NOT NULL,
  `nombre_persona` varchar (100) NOT NULL,
  `apellido_paterno` varchar(100) NOT NULL,
  `apellido_materno` varchar(100) NOT NULL,
  `email` varchar(200) NOT NULL,
  `ocupacion` varchar(200) NOT NULL,
  `tipo_de_sangre` varchar(10) DEFAULT NULL,
  `id_genero` int NOT NULL
FOREIGN KEY (`id_genero`) REFERENCES `tb_genero` (`id_genero`);
)

INSERT INTO tb_persona (nombre_persona, apellido_paterno, apellido_materno, email, ocupacion, tipo_de_sangre, id_genero) 
VALUES('José', 'Malagón', 'Gonzalez', 'jose.malagon@continental.mx', 'Cerrajero', 'O positivo', 1
)


CREATE TABLE `tb_paciente` (
  `id_paciente` int NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `enfermedades_cronicas` varchar(200) DEFAULT NULL,
  `alergias` varchar(200) DEFAULT NULL,
  `antecedentes_familiares` varchar(200) DEFAULT NULL,
  `id_persona` int NOT NULL
FOREIGN KEY (`id_persona`) REFERENCES `tb_personas` (`id_persona`);
)

INSERT INTO tb_paciente (fecha_nacimiento, enfermedades_cronicas, alergias, antecedentes_familiares, id_persona) 
VALUES('2000/05/12', 'Obesidad y Hipertensión Arterial', 'Penicilina', 'Diabetes', 1
)


CREATE TABLE `tb_medico` (
  `id_medico` int identity(1,1) NOT NULL,
  `RFC` varchar(100) NOT NULL,
  `cedula_profesional` varchar(100) NOT NULL,
  `password` varchar(200) NOT NULL,
  `posicion` varchar(100) NOT NULL,
  `id_rol` int NOT NULL,
  `id_persona` int NOT NULL,
FOREIGN KEY (`id_rol`) REFERENCES `tb_rol` (`id_rol`)
FOREIGN KEY (`id_persona`) REFERENCES `tb_personas` (`id_persona`)
)

INSERT INTO tb_medico (RFC, cedula_profesional, password, posicion, id_rol, id_persona) 
VALUES('LUBN900612', '2625J620', '123456ABC', 'Cirujano', 1, 2
)


CREATE TABLE `tb_relacion` (
  `id_relacion` int NOT NULL,
  `id_paciente` int NOT NULL,
  `id_medico` int NOT NULL,
FOREIGN KEY (`id_paciente`) REFERENCES `tb_paciente` (`id_paciente`)
FOREIGN KEY (`id_medico`) REFERENCES `tb_medico` (`id_medico`)
)
INSERT INTO tb_relacion (id_paciente, id_medico) 
VALUES(1,1)
)
