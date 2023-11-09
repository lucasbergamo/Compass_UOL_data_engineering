
-- criando a tabela de clientes, quando indiquei a primary key na criação, 
-- houve um erro ao copiar para outra tabela, vou mudar a abordagem

CREATE TABLE tb_cliente (
    idCliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(20),
    estadoCliente VARCHAR(2),
    paisCliente VARCHAR(20)
   )

-- copiando os dados para a nova tabela

INSERT INTO tb_cliente (nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT nomeCliente, cidadeCliente,estadoCliente, paisCliente
FROM tb_locacao

-- criando tabela carros, tive de colocar id carro com auto incremento do id, pois deu erro de todas as outras formas

CREATE TABLE tb_carro(
    idCarro INTEGER PRIMARY KEY AUTOINCREMENT,
    kmCarro INT,
    classiCarro VARCHAR(20),
    marcaCarro VARCHAR(20),
    modeloCarro VARCHAR(20),    
    anoCarro INT
    )

INSERT INTO tb_carro (kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro)
SELECT DISTINCT kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro
FROM tb_locacao

-- criando tabela combustivel

CREATE TABLE tb_combustivel(
    idCombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(20)
    )

INSERT INTO tb_combustivel (idCombustivel, tipoCombustivel)
SELECT DISTINCT idCombustivel, tipoCombustivel
FROM tb_locacao

-- Criando a tabela vendedor

CREATE TABLE tb_vendedor(
    idVendedor INTEGER PRIMARY KEY AUTOINCREMENT,
    nomeVendedor VARCHAR(100),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(20)
    )

INSERT INTO tb_vendedor(nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao

-- Criando a tabela locacao

CREATE TABLE locacao (
    idLocacao INTEGER PRIMARY KEY AUTOINCREMENT,
    dataLocacao DATETIME,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL,
    dataEntrega DATE,
    horaEntrega TIME,
    idCombustivel INT,
    idCliente INT,
    idVendedor INT,
    idCarro INT,
    FOREIGN KEY (idCarro) REFERENCES tb_carro(idCarro),
    FOREIGN KEY (idCombustivel) REFERENCES tb_combustivel(idCombustivel),
    FOREIGN KEY (idCliente) REFERENCES tb_cliente(idCliente),
    FOREIGN KEY (idVendedor) REFERENCES tb_vendedor(idVendedor)
    )

INSERT INTO locacao (
    dataLocacao, 
    horaLocacao, 
    qtdDiaria, 
    vlrDiaria, 
    dataEntrega, 
    horaEntrega, 
    idCombustivel, 
    idCliente, 
    idVendedor, 
    idCarro
    )
    
SELECT 
    dataLocacao,
    horaLocacao,
    qtdDiaria,
    vlrDiaria,
    dataEntrega,
    horaEntrega,
    idCombustivel,
    idCliente,
    idVendedor,
    idCarro
    
FROM tb_locacao

-- Deletando a tabela original e alterando o nome

DROP TABLE tb_locacao

ALTER TABLE locacao RENAME TO tb_locacao


CREATE TABLE combustivel(
    idCombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(20)
    )

INSERT INTO tb_combustivel (idCombustivel, tipoCombustivel)
SELECT DISTINCT idCombustivel, tipoCombustivel
FROM tb_locacao
