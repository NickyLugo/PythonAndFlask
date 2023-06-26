USE db_clinica_S181;

CREATE TABLE `tb_cat_rol` (
  `id_rol` INT NOT NULL AUTO_INCREMENT,
  `nombre_rol` varchar (100) NOT NULL,
  PRIMARY KEY (id_rol)
); 

INSERT INTO tb_cat_rol (nombre_rol) 
VALUES('Administrador'), ('Usuario');

CREATE TABLE `tb_cat_genero` (
  `id_genero` INT NOT NULL AUTO_INCREMENT,
  `nombre_genero` varchar (100) NOT NULL,
  PRIMARY KEY (id_genero)
);

INSERT INTO tb_cat_genero (nombre_genero) 
VALUES('Hombre'), ('Mujer'), ('Otro');

CREATE TABLE `tb_persona` (
  `id_persona` INT NOT NULL AUTO_INCREMENT,
  `nombre_completo` varchar (200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `ocupacion` varchar(200) NOT NULL,
  `tipo_de_sangre` varchar(10) DEFAULT NULL,
  `id_genero` INT NOT NULL,
  FOREIGN KEY (`id_genero`) REFERENCES `tb_cat_genero` (`id_genero`),
  PRIMARY KEY (id_persona)
);

INSERT INTO tb_persona (nombre_completo, email, ocupacion, tipo_de_sangre, id_genero) 
VALUES('José Malagón Gonzalez', 'jose.malagon@continental.mx', 'Cerrajero', 'O positivo', 1);
INSERT INTO tb_persona (nombre_completo, email, ocupacion, tipo_de_sangre, id_genero) 
VALUES('Nick Pérez Prado', 'nick.pp@continental.mx', 'Dueño', 'O positivo', 1);

CREATE TABLE `tb_paciente` (
  `id_paciente` INT NOT NULL AUTO_INCREMENT,
  `fecha_nacimiento` date NOT NULL,
  `enfermedades_cronicas` varchar(200) DEFAULT NULL,
  `alergias` varchar(200) DEFAULT NULL,
  `antecedentes_familiares` varchar(200) DEFAULT NULL,
  `id_persona` INT NOT NULL,
  FOREIGN KEY (`id_persona`) REFERENCES `tb_persona` (`id_persona`),
  PRIMARY KEY (id_paciente)
);

INSERT INTO tb_paciente (fecha_nacimiento, enfermedades_cronicas, alergias, antecedentes_familiares, id_persona) 
VALUES('2000-05-12', 'Obesidad y Hipertensión Arterial', 'Penicilina', 'Diabetes', 1);

CREATE TABLE `tb_medico` (
  `id_medico` INT NOT NULL AUTO_INCREMENT,
  `RFC` varchar(100) NOT NULL,
  `cedula_profesional` varchar(100) NOT NULL,
  `password` varchar(200) NOT NULL,
  `posicion` varchar(100) NOT NULL,
  `id_rol` INT NOT NULL,
  FOREIGN KEY (`id_rol`) REFERENCES `tb_cat_rol` (`id_rol`),
  PRIMARY KEY (id_medico)
);

INSERT INTO tb_medico (RFC, cedula_profesional, password, posicion, id_rol, id_persona) 
VALUES('LUBN900612', '2625J620', '123456ABC', 'Cirujano', 1, 2);

CREATE TABLE `tb_rel_medico_paciente` (
  `id_rel_medico_paciente` INT NOT NULL AUTO_INCREMENT,
  `id_paciente` INT NOT NULL,
  `id_medico` INT NOT NULL,
  FOREIGN KEY (`id_paciente`) REFERENCES `tb_paciente` (`id_paciente`),
  FOREIGN KEY (`id_medico`) REFERENCES `tb_medico` (`id_medico`),
  PRIMARY KEY (id_rel_medico_paciente)
);

INSERT INTO tb_rel_medico_paciente (id_paciente, id_medico) 
VALUES(1,1);