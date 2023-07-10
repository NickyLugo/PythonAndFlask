
CREATE TABLE `tb_persona` (
  `id_persona` INT NOT NULL AUTO_INCREMENT,
  `nombre` varchar (200) NOT NULL,
  `apellido_paterno` varchar (100) NOT NULL,
  `apellido_materno` varchar (100) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `carrera` varchar (150) NOT NULL,
  `email` varchar(200) NOT NULL,
  `telefono` INT NOT NULL,
  PRIMARY KEY (id_persona)
);

