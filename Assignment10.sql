drop table if exists as10_book_0nf;
/* Create Table as10_book_0nf */
CREATE TABLE as10_book_0nf (
    isbn                varchar(200)    not null,
    title               varchar(200)    not null,
    author              varchar(200)    not null,
    author_nationality  varchar(200)    not null,
    format              varchar(200)    not null,
    price               numeric(5, 2)   not null,
    subject             varchar(200)    not null,
    pages               int             not null,
    thickness           varchar(200)    not null,
    publisher           varchar(200)    not null,
    publisher_country   varchar(200)    not null,
    genre_id            int             not null,
    genre_name          varchar(200)    not null
);
/* INSERT into as10_book_0nf */
INSERT INTO as10_book_0nf values (
    '1590593324',
    'Beginning MySQL Database Design and Optimization',
    'Chad Russell',
    'American',
    'Hardcover',
    49.99,
    'MySQL, Database, Design',
    520,
    'Thick',
    'Apress',
    'USA',
    1,
    'Tutorial'
);

/* Return rows for as10_book_0nf */
SELECT * FROM as10_book_0nf;

drop table if exists as10_book_1nf;
/* Create Table as10_book_1nf */
CREATE TABLE as10_book_1nf (
    isbn                varchar(200)    not null,
    title               varchar(200)    not null,
    author              varchar(200)    not null,
    author_nationality  varchar(200)    not null,
    format              varchar(200)    not null,
    price               numeric(5, 2)   not null,
    pages               int             not null,
    thickness           varchar(200)    not null,
    publisher           varchar(200)    not null,
    publisher_country   varchar(200)    not null,
    genre_id            int             not null,
    genre_name          varchar(200)    not null
);

/* INSERT into as10_book_1nf */
INSERT INTO as10_book_1nf
SELECT isbn, title, author, author_nationality, format, price, pages,
       thickness, publisher, publisher_country, genre_id, genre_name
FROM as10_book_0nf;

drop table if exists as10_subject_1nf;
/* Create Table as10_subject_1nf */
CREATE TABLE as10_subject_1nf (
    isbn                varchar(200)    not null,
    subject             varchar(200)    not null
);

/* INSERT into as10_subject_1nf */
INSERT INTO as10_subject_1nf VALUES
('1590593324', 'MySQL'),
('1590593324', 'Database'),
('1590593324', 'Design');

/* Retrieve rows from as10_book_1nf */
select * from as10_book_1nf;

/* Retrieve rows from as10_subject_1nf */
select * from as10_subject_1nf;

drop table if exists as10_book2_1nf;
/* Create Table as10_book_1nf */
CREATE TABLE as10_book2_1nf (
    title               varchar(200)    not null,
    format              varchar(200)    not null,
    author              varchar(200)    not null,
    author_nationality  varchar(200)    not null,
    price               numeric(5, 2)   not null,
    pages               int             not null,
    thickness           varchar(200)    not null,
    publisher           varchar(200)    not null,
    publisher_country   varchar(200)    not null,
    genre_id            int             not null,
    genre_name          varchar(200)    not null
);

/* INSERT into as10_book2_1nf */
INSERT INTO as10_book2_1nf values
(
    'Beginning MySQL Database Design and Optimization',
    'Hardcover',
    'Chad Russell',
    'American',
    49.99,
    520,
    'Thick',
    'Apress',
    'USA',
    1,
    'Tutorial'
),
(
    'Beginning MySQL Database Design and Optimization',
    'E-book',
    'Chad Russell',
    'American',
    49.99,
    520,
    'Thick',
    'Apress',
    'USA',
    1,
    'Tutorial'
),
(
    'The Relational Model for Database Management: Version 2',
    'E-book',
    'E.F.Codd',
    'British',
    13.88,
    538,
    'Thick',
    'Addison-Wesley',
    'USA',
    2,
    'Popular science'
),
(
    'The Relational Model for Database Management: Version 2',
    'Paperback',
    'E.F.Codd',
    'British',
    13.88,
    538,
    'Thick',
    'Addison-Wesley',
    'USA',
    2,
    'Popular science'
);

/* Retrieve rows from as10_book2_1nf */
select * from as10_book2_1nf;

drop table if exists as10_book2_2nf;
/* Create Table as10_book_1nf */
CREATE TABLE as10_book2_2nf (
    title               varchar(200)    not null,
    author              varchar(200)    not null,
    author_nationality  varchar(200)    not null,
    pages               int             not null,
    thickness           varchar(200)    not null,
    publisher           varchar(200)    not null,
    publisher_country   varchar(200)    not null,
    genre_id            int             not null,
    genre_name          varchar(200)    not null
);

/* INSERT into as10_book_1nf */
INSERT INTO as10_book2_2nf
SELECT DISTINCT
    title, author, author_nationality, pages,
    thickness, publisher, publisher_country, genre_id, genre_name
FROM as10_book2_1nf;

drop table if exists as10_price2_2nf;
/* Create Table as10_book_1nf */
CREATE TABLE as10_price2_2nf
(
    title  varchar(200)  not null,
    format varchar(200)  not null,
    price  numeric(5, 2) not null
);

/* INSERT into as10_book_1nf */
INSERT INTO as10_price2_2nf
SELECT title, format, price
FROM as10_book2_1nf;

/* Retrieve rows from as10_book2_2nf */
select * from as10_book2_2nf;

/* Retrieve rows from as10_price2_2nf */
select * from as10_price2_2nf;

drop table if exists as10_book_3nf;
/* Create Table as10_book_3nf */
CREATE TABLE as10_book_3nf (
    title               varchar(200)    not null,
    author              varchar(200)    not null,
    pages               int             not null,
    thickness           varchar(200)    not null,
    publisher           varchar(200)    not null,
    genre_id            int             not null
);

/* INSERT into as10_book_3nf */
INSERT INTO as10_book_3nf
SELECT DISTINCT
    title, author, pages, thickness, publisher, genre_id;
FROM as10_book2_2nf;

/* Retrieve rows from as10_book_3nf */
select * from as10_book_3nf;

drop table if exists as10_price_3nf;
/* Create Table as10_book_1nf */
CREATE TABLE as10_price_3nf
(
    title  varchar(200)  not null,
    format varchar(200)  not null,
    price  numeric(5, 2) not null
);

/* INSERT into as10_price_3nf */
INSERT INTO as10_price_3nf
SELECT title, format, price
FROM as10_price2_2nf;

/* Retrieve rows from as10_price3_3nf */
select * from as10_price_3nf;

drop table if exists as10_author_3nf;
/* Create Table as10_author_3nf */
CREATE TABLE as10_author_3nf
(
    author              varchar(200)    not null,
    nationality         varchar(200)    not null
);

/* INSERT into as10_price_3nf */
INSERT INTO as10_author_3nf
SELECT author, author_nationality
FROM as10_book2_2nf;

/* Retrieve rows from as10_author_3nf */
select * from as10_author_3nf;

drop table if exists as10_publisher_3nf;
/* Create Table as10_publisher_3nf */
CREATE TABLE as10_publisher_3nf
(
    publisher               varchar(200)    not null,
    country                 varchar(200)    not null
);

/* INSERT into as10_publisher_3nf */
INSERT INTO as10_publisher_3nf
SELECT publisher, publisher_country
FROM as10_book2_2nf;

/* Retrieve rows from as10_publisher_3nf */
select * from as10_publisher_3nf;

--     genre_name          varchar(200)    not null

drop table if exists as10_genre_3nf;
/* Create Table as10_publisher_3nf */
CREATE TABLE as10_genre_3nf
(
    genre_id             int             not null,
    name                 varchar(200)    not null
);

/* INSERT into as10_genre_3nf */
INSERT INTO as10_genre_3nf
SELECT genre_id, genre_name
FROM as10_book2_2nf;

/* Retrieve rows from as10_genre_3nf */
select * from as10_genre_3nf;