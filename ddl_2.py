DDL_QUERY2 = '''
CREATE TABLE IF NOT EXISTS dim_producto (
	idarticulo INT PRIMARY KEY,
	idcategoria INT,
	codigo VARCHAR(50),
	nombre_producto VARCHAR(100),
	precio_venta DECIMAL(11, 2),
	stock INT,
	descripcion_producto VARCHAR(255),
	imagen VARCHAR(20),
	estado_producto BIT,
	nombre_categoria VARCHAR(50),
	descripcion_categoria VARCHAR(255),
	estado_categoria BIT
);

CREATE TABLE IF NOT EXISTS dim_colaborador (
	idusuario INT PRIMARY KEY,
	idrol INT,
	nombre_colaborador VARCHAR(100),
	tipo_documento VARCHAR(20),
	num_documento VARCHAR(20),
	direccion VARCHAR(70),
	telefono VARCHAR(20),
	email VARCHAR(50),
	clave VARBINARY(10),
	estado_colaborador BIT,
	nombre_rol VARCHAR(30),
	descripcion VARCHAR(255),
	estado_rol BIT
);

CREATE TABLE IF NOT EXISTS dim_persona (
	idpersona INT PRIMARY KEY,
	tipo_persona VARCHAR(20),
	nombre VARCHAR(100),
	tipo_documento VARCHAR(20),
	num_documento VARCHAR(20),
	direccion VARCHAR(70),
	telefono VARCHAR(20),
	email VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS fact_venta (
	idventa INT PRIMARY KEY,
	idcliente INT,
	idusuario INT,
	tipo_comprobante VARCHAR(20),
	serie_comprobante VARCHAR(7),
	num_comprobante VARCHAR(10),
	fecha TIMESTAMP,
	impuesto DECIMAL(4, 2),
	total DECIMAL(11, 2),
	estado VARCHAR(20),

CONSTRAINT fk_idusuario
FOREIGN KEY (idusuario)
            REFERENCES dim_colaborador(idusuario),

CONSTRAINT fk_idcliente
FOREIGN KEY (idcliente)
            REFERENCES dim_persona(idpersona)
);

CREATE TABLE IF NOT EXISTS fact_ingreso (
	idingreso INT PRIMARY KEY,
	idproveedor INT,
	idusuario INT,
	tipo_comprobante VARCHAR(20),
	serie_comprobante VARCHAR(7),
	num_comprobante VARCHAR(10),
	fecha TIMESTAMP,
	impuesto DECIMAL(4 ,2),
	total DECIMAL(11, 2),
	estado VARCHAR(20),

	CONSTRAINT fk_idproveedor
	FOREIGN KEY (idproveedor)
	REFERENCES dim_persona(idpersona),
	
	CONSTRAINT fk_idusuario_2
	FOREIGN KEY (idusuario)
	REFERENCES dim_colaborador(idusuario)
);

CREATE TABLE IF NOT EXISTS dim_ingreso(
	iddetalle_ingreso INT PRIMARY KEY,
	idingreso INT,
	idarticulo INT,
	cantidad INT,
	precio DECIMAL(11, 2),

	CONSTRAINT fk_idarticulo
	FOREIGN KEY (idarticulo)
	REFERENCES dim_producto(idarticulo),

	CONSTRAINT fk_idingreso
	FOREIGN KEY (idingreso)
	REFERENCES fact_ingreso(idingreso)
);

CREATE TABLE IF NOT EXISTS dim_venta(
	iddetalle_venta INT PRIMARY KEY,
	idventa INT,
	idarticulo INT,
	cantidad INT,
	precio DECIMAL(11, 2),
	descuento DECIMAL(11, 2),

CONSTRAINT fk_idarticulo_2
FOREIGN KEY (idarticulo)
            REFERENCES dim_producto(idarticulo),

CONSTRAINT fk_idventa
FOREIGN KEY (idventa)
            REFERENCES fact_venta(idventa)
);
'''