drop database if exists restaurante_bd;
create database restaurante_bd;
use restaurante_bd;

create table mesas(
	nroMesa integer,
    nroPessoas integer,
    constraint pk_mesa primary key (nroMesa)
);

create table clientes(
	idCli integer auto_increment,
    nome varchar(50),
    telefone varchar(20),
    cpf varchar (15),
    unique (cpf),
    constraint pk_cliente primary key (idCli)
);

create table reservas(
	idReser integer auto_increment,
    idCli integer not null,
    nroMesa integer not null,
    datas date,
    hora time,
    nroPessoas integer,
    constraint pk_reservas primary key (idReser),
    constraint fk_reservas foreign key (idCli) references clientes(idCli),
    constraint fk_reMesa_mesa foreign key (nroMesa) references mesas (nroMesa)
);

create table funcionarios(
	cpf integer,
    salario float,
    situacao varchar(50) not null,
    nome varchar(50),
    constraint pk_fun primary key  (cpf)
);

create table garcons(
	cpf integer,
    constraint pk_gar primary key (cpf),
    constraint fk_gar foreign key (cpf) references funcionarios (cpf)
);

create table cozinheiros(
	cpf integer,
    cpfChefe integer,
    constraint pk_coz primary key (cpf),
    constraint fk_coz foreign key (cpf) references funcionarios (cpf),
    constraint fk_chefe foreign key (cpfChefe) references cozinheiros (cpf)
);

create table pedidos(
	idPed integer auto_increment,
    situacao varchar(50),
    idCli integer not null,
    cpfGar integer not null,
    dataPed date,
    constraint pk_ped primary key (idPed),
    constraint fk_pedGar foreign key (cpfGar) references garcons(cpf),
    constraint fk_cli foreign key (idCli) references clientes(idCli)
);

create table pratos (
	id integer auto_increment,
    nome varchar(50),
    constraint pk_pratos primary key (id)
);

create table pedidos_pratos(
	idPratos integer,
    idPed integer,
    qtd integer,
    constraint pk_pedPratos primary key (idPratos, idPed),
    constraint fk_pedPratos_ped foreign key (idPed) references pedidos (idPed),
    constraint fk_pedPratos_pratos foreign key (idPratos) references pratos (id)
);

create table ingredientes(
	id integer auto_increment,
    nome varchar(50),
    constraint pk_ingredientes primary key (id)
);

create table pratos_ingrediente(
	idIng integer,
	idPratos integer,
	qtd integer,
	constraint pk_pratIng primary key (idIng, idPratos),
	constraint fk_pratIng_ing foreign key (idIng) references ingredientes (id),
	constraint pk_pratIng_prat foreign key (idPratos) references pratos (id)
);

create table fornecedores(
	id integer auto_increment,
    nome varchar(50),
    telefone varchar(20),
    constraint pk_fornecedores primary key (id)
);

create table ingredientes_fornecedores(
	idForn integer,
    idIng integer,
    constraint pk_ingForn primary key (idForn, idIng),
    constraint fk_ingForn_forn foreign key (idForn) references fornecedores (id),
    constraint fk_ingForn_ing foreign key (idIng) references ingredientes (id)
);

-- inserts

insert into mesas(nroMesa, nroPessoas) values (1, 4), (2, 4), (3, 8), (4, 8), (5, 6);
insert into clientes(nome, telefone, cpf) value ('Astolfo da Silva', '99999-9999', '121312312'), ('John Smith', '07700 900461', '3454523'), ('Mat Smith', '07700 900461', '45898989'), ('Peter Capaldi', '07700 900461', '78797979');
insert into reservas(idCli, datas, hora, nroPessoas, nroMesa) values (1, '2017-10-12', '20:00:00', 2, 2), (2, '1998-10-15', '17:00:00', 2, 3), (2, '3012-10-15', '17:00:00', 3, 3);
insert into funcionarios(cpf, salario, situacao, nome) values (1, 3000, 'Ativo', 'Master chefe'), (2, NULL, 'Aposentado', 'Mario Verde'), (3, 1000, 'Ativo', 'Mario Mario'), (4, NULL, 'Estagiario', 'Luigi Mario');
insert into garcons(cpf) values (1), (2);
insert into cozinheiros (cpf, cpfChefe) values (3, NULL), (4, 3);
insert into pedidos (situacao, idCli, cpfGar, dataPed) values ('pendente', 2, 1, CURDATE()), ('pago', 2, 2, CURDATE());
insert into pratos (nome) values ('Macarrao instantaneo'), ('Pizza congelada'), ('Milk Shake');
insert into pedidos_pratos (idPratos, idPed, qtd) values (1, 1, 3), (2, 2, 1), (2, 1, 7);
insert into ingredientes (nome) values ('Cebola'), ('Chocolate');
insert into pratos_ingrediente (idIng, idPratos, qtd) values (2, 3, 2);
insert into fornecedores (nome, telefone) values ('Bob da Silva', '99999-9999'), ('Carlos da Silva', '99999-9900'), ('Bob Smith', '99999-0000');
insert into ingredientes_fornecedores (idForn, idIng) values (1, 2), (2, 2), (3, 2), (1, 1);
