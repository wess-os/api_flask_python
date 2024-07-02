CREATE SCHEMA `alunos`;

USE alunos;

CREATE TABLE alunos (
    id INTEGER NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100),
    idade INTEGER,
    PRIMARY KEY (id)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;