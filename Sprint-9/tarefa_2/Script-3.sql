-- criando medida fato_locacao

create table fato_locacao (
	idLocacao INT PRIMARY KEY,
	idCliente INT, 
	idCarro INT, 
	idVendedor INT,
	idCombustivel INT,
	FOREIGN KEY (idCliente) REFERENCES dim_cliente(idCliente), 
	FOREIGN KEY (idCarro) REFERENCES dim_carro(idCarro), 
	FOREIGN KEY (idVendedor) REFERENCES dim_vendedor(idVendedor),
	FOREIGN KEY (idCombustivel) REFERENCES dim_combustivel(idCombustivel),
	FOREIGN KEY (idLocacao) REFERENCES dim_locacao(idLocacao)
	)

-- inserindo os dados na medida locacao	
	
INSERT INTO fato_locacao (idLocacao, idCliente, idCarro, idVendedor, idCombustivel)
SELECT idLocacao, idCliente, idCarro, idVendedor,idCombustivel
FROM tb_locacao

SELECT * from fato_locacao

-- criando o contexto locacao

create table dim_locacao (
	idLocacao INT PRIMARY KEY, 
	qtdDiaria INT,
	vlrDiaria DECIMAL,
	dataLocacao DATETIME,
	horaLocacao TIME,
	dataEntrega DATE,
	horaEntrega TIME
	)

-- inserindo informações no contexto cliente	
	
INSERT INTO dim_locacao (idLocacao, qtdDiaria, vlrDiaria, dataLocacao, horaLocacao, dataEntrega, horaEntrega)
SELECT idLocacao, qtdDiaria, vlrDiaria, dataLocacao, horaLocacao, dataEntrega, horaEntrega
FROM tb_locacao


-- criando o contexto cliente

create table dim_cliente (
	idCliente INT PRIMARY KEY, 
	nomeCliente VARCHAR(255), 
	cidadeCliente VARCHAR(255),
	estadoCliente VARCHAR(2),
    paisCliente VARCHAR(20)
	)

-- inserindo informações no contexto cliente	
	
INSERT INTO dim_cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_cliente

-- criando o contexto carro

CREATE TABLE dim_carro (
    idCarro INTEGER PRIMARY KEY,
    kmCarro INT,
    classiCarro VARCHAR(20),
    marcaCarro VARCHAR(20),
    modeloCarro VARCHAR(20),
    anoCarro INT
)


-- inserindo informações no contexto carro

INSERT INTO dim_carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro)
SELECT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro
FROM tb_carro


-- criando o contexto carro

CREATE TABLE dim_vendedor (
    idVendedor INTEGER PRIMARY KEY,
    nomeVendedor VARCHAR(100),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(20)
)

-- inserindo informações no contexto carro

INSERT INTO dim_vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_vendedor


-- criando o contexto combustivel

CREATE TABLE dim_combustivel (
    idCombustivel INTEGER PRIMARY KEY,
    tipoCombustivel VARCHAR(20)
    )

INSERT INTO dim_combustivel (idCombustivel, tipoCombustivel)
SELECT idCombustivel, tipoCombustivel
FROM tb_combustivel

-- inserindo informações no contexto combustivel

INSERT INTO dim_vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_vendedor


-- Criando Views

create view statusLocacao as
select * from dim_locacao

create view statusCliente as
select * from dim_cliente

create view statusVendedor as
select * from dim_vendedor

create view statusCarro as
select 
    C.*,
    CB.tipoCombustivel
from 
    dim_carro C
join
    dim_combustivel CB on C.idCarro = CB.idCombustivel

