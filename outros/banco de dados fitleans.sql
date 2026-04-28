

CREATE DATABASE fitlens_db;

USE fitlens_db;

CREATE TABLE planos (
    id_plano INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    descricao TEXT
);

CREATE TABLE unidades (
    id_unidade INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    cidade VARCHAR(100),
    estado VARCHAR(50)
);

CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    telefone VARCHAR(20),
    plano_id INT,
    FOREIGN KEY (plano_id) REFERENCES planos(id_plano)
);

CREATE TABLE franquias (
    id_franquia INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    telefone VARCHAR(20),
    cidade_interesse VARCHAR(100)
);

SELECT * FROM clientes;
