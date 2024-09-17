CREATE DATABASE rag;

CREATE EXTENSION vector;

CREATE TABLE rag.dbo.documents(
    id INT PRIMARY KEY NOT NULL,
    document BYTEA NOT NULL
)

