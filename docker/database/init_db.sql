create extension vector;

create schema rag;

create table rag.documents(
	document_id int generated always as identity,
    document_file bytea not null,
	primary key(document_id)
);

create table rag.embeddings(
	embedding_id int generated always as identity,
    vector vector(4096) not null,
	doc varchar(500) not null,
	document_id int not null,
	constraint document_id
      foreign key(document_id) 
        references rag.documents(document_id)	
);